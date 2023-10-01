/** @format */

import React, {useEffect, useState} from "react";
import {socket} from "../socket";
import { Timer } from "./Timer";
import { object, string, number } from 'zod';
import { useForm } from 'react-hook-form';
import { zodResolver } from '@hookform/resolvers/zod';
import { useParticipantForm } from "../stores/useParticipantForm";
import { CustomInput } from "./CustomInput";
import { useEventForm } from "../stores/useEventForm";


interface Event {
	id?: number;
	startnumber: number;
	license_plate: string;
	start_timestamp: number;
	end_timestamp: number;
	distance: number;
	speed: number;
	session_name: string;
}

const formSchema = object({
	startnumber: number(),
	license_plate: string().min(1, 'Licenseplate is required'),
	distance: number(),
	speed: number(),
	sessionName: string().min(1, 'Eventname is required')
  });

export function SessionManager() {
	const [ready, setReady] = useState<boolean>(false);
	const [startTimestamp, setStartTimestamp] = useState<number | null>(null);
	const [endTimestamp, setEndTimestamp] = useState<number | null>(null);
	const [currentTimestamp, setCurrentTimestamp] = useState<number | null>(null);

	const [events, setEvents] = useState<Event[]>([]);

	const { register, handleSubmit, setValue, resetField, formState: { errors } } = useForm({
		resolver: zodResolver(formSchema),
	  });

	  const { startNumber, licensePlate, setStartNumber, setLicensePlate, clearForm } = useParticipantForm();


	  const { distance, speed, sessionName, setDistance, setSpeed, setSessionName } = useEventForm();
	  const onSubmit = (data: any) => {
		sendReady();
	  };


	function sendReady() {
		setStartTimestamp(0);
		setEndTimestamp(0);
		socket.emit("ready");
	}

	function saveEvent() {
		socket.emit( "save", {
			startnumber: startNumber, 
			license_plate: licensePlate, 
			start: startTimestamp, 
			stop: endTimestamp,
			distance: distance,
			speed: speed,
			session_name: sessionName
		});
	}


	useEffect(() => {
		const onReady = (data: any) => {
			setReady(data.ready);
		};

		const onStart = (data: any) => {
			setStartTimestamp(data.start);
		};

		const onStop = (data: any) => {
			setEndTimestamp(data.stop);
		};

		const onTimestamp = (data: any) => {
			setCurrentTimestamp(data.timestamp)
		}
		
		const onSave = (data: any) => {
			setEvents([...events, {
				distance: distance,
				speed: speed,
				start_timestamp: startTimestamp ? startTimestamp : 0,
				end_timestamp: endTimestamp ? endTimestamp : 0,
				license_plate: licensePlate,
				startnumber: startNumber,
				session_name: sessionName
			}])
			resetField("startnumber");
			resetField("license_plate")
			clearForm();
		}

		const onEvents = (data: any) => {
			setEvents(data.events);
		}

		socket.on("ready", onReady);
		socket.on("start", onStart);
		socket.on("stop", onStop);
		socket.on("timestamp", onTimestamp);
		socket.on("save", onSave);
		socket.on("events", onEvents);



		return () => {
			socket.off("ready", onReady);
			socket.off("start", onStart);
			socket.off("stop", onStop);
			socket.off("timestamp", onTimestamp);
			socket.off("save", onSave);
			socket.off("events", onEvents);
		};
	}, []);

	useEffect(() => {
		if (endTimestamp) {
			saveEvent();
		}
	}, [endTimestamp])


	useEffect(() => {
		console.log(errors);
	}, [errors])

	


	return (
		<>
		    <form onSubmit={handleSubmit(onSubmit)} className="flex flex-col gap-2 p-4">
				<div className="flex gap-2 p-4">
					<CustomInput register={register} name={"distance"} label={"Distance"} change={(e) => setDistance(parseInt(e.target.value))} type="number" className="flex-1" />
					<CustomInput register={register} name={"speed"} label={"Speed"} change={(e) => setSpeed(parseInt(e.target.value))} type="number" />
					<CustomInput register={register} name={"sessionName"} label={"Eventname"} change={(e) => setSessionName(e.target.value)} />
				</div>
				<div className="flex gap-2 p-4">
					<CustomInput register={register} name={"startnumber"} label={"Startnumber"} change={(e) => setStartNumber(parseInt(e.target.value))} type="number" />
					<CustomInput register={register} name={"license_plate"} label={"Licenseplate"} change={(e) => setLicensePlate(e.target.value)} />
				</div>



				
				<div className="flex justify-center items-center">
					<button
						disabled={ready}
						type="submit"
						className="rounded-md bg-indigo-500 px-3.5 py-2.5 text-sm font-semibold text-white shadow-sm hover:bg-indigo-400 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-500 disabled:bg-red-200"
					>
						READY
					</button>
				</div>

			</form>

			<span>{ready ? "System is ready" : "System is not ready yet"}</span>
			<Timer start={startTimestamp} end={endTimestamp} timestamp={currentTimestamp} />
			<div>
				{events.sort((a: Event, b: Event) => (new Date(b.end_timestamp)).getTime() - (new Date(a.end_timestamp)).getTime()).map((event, index) => <div key={index}>{event.startnumber} {event.license_plate} {event.start_timestamp} {event.end_timestamp}</div>)}
			</div>
		</>
	);
}
