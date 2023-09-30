/** @format */

import React, {useEffect, useState} from "react";
import {socket} from "../socket";
import { Timer } from "./Timer";
import { object, string, number } from 'zod';
import { useForm } from 'react-hook-form';
import { zodResolver } from '@hookform/resolvers/zod';
import { useParticipantForm } from "../stores/useParticipantForm";


interface Event {
	id: number;
	startnumber: string;
	license_plate: string;
	start_timestamp: string;
	end_timestamp: string;
	distance: number;
	speed: number;
	session_name: string;
}

const formSchema = object({
	startnumber: string().min(1, 'Startnumber is required'),
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

	const { register, handleSubmit, setValue, formState: { errors } } = useForm({
		resolver: zodResolver(formSchema),
	  });

	  const { startNumber, licensePlate, distance, speed, sessionName, setStartNumber, setLicensePlate, setDistance, setSpeed, setSessionName } = useParticipantForm();

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
			setEvents(data.events.sort((a: Event, b: Event) => b.id - a.id));
		}

		socket.on("ready", onReady);
		socket.on("start", onStart);
		socket.on("stop", onStop);
		socket.on("timestamp", onTimestamp);
		socket.on("save", onSave);



		return () => {
			socket.off("ready", onReady);
			socket.off("start", onStart);
			socket.off("stop", onStop);
			socket.off("timestamp", onTimestamp);
			socket.off("save", onSave);
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
		    <form onSubmit={handleSubmit(onSubmit)}>
				<div>
					<label htmlFor="startnumber">Startnumber: </label>
					<input
					{...register('startnumber')}
					onChange={(e) => setStartNumber(e.target.value)}
					/>
				</div>
				
				<div>
					<label htmlFor="license_plate">Licenseplate: </label>
					<input
					{...register('license_plate')}
					onChange={(e) => setLicensePlate(e.target.value)}
					/>
					
				</div>

				<div>
					<label htmlFor="distance">Distance: </label>
					<input
						{...register('distance', {
							setValueAs: (value) => Number(value),
						})}
						type="number"
						onChange={(e) => setDistance(parseInt(e.target.value))}
						/>
					
				</div>

				<div>
					<label htmlFor="speed">Speed: </label>
					<input
						{...register('speed', {
							setValueAs: (value) => Number(value),
						  })}
						  type="number"
						  onChange={(e) => setSpeed(parseInt(e.target.value))}
						/>
					
				</div>

				<div>
					<label htmlFor="sessionName">Eventname: </label>
					<input
					{...register('sessionName')}
					onChange={(e) => setSessionName(e.target.value)}
					/>
					
				</div>
				
				<button
					disabled={ready}
					type="submit"
					className="rounded-md bg-indigo-500 px-3.5 py-2.5 text-sm font-semibold text-white shadow-sm hover:bg-indigo-400 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-500 disabled:bg-red-200"
				>
					Ready
				</button>
				</form>

			<span>{ready ? "System is ready" : "System is not ready yet"}</span>
			<Timer start={startTimestamp} end={endTimestamp} timestamp={currentTimestamp} />
			<div>
				{events.map((event, index) => <div key={index}>{event.startnumber} {event.license_plate} {event.start_timestamp} {event.end_timestamp}</div>)}
			</div>
		</>
	);
}
