import { create } from 'zustand'

interface ParticipantFormProps {
    startNumber: string;
    licensePlate: string;
    distance: number;
    speed: number;
    sessionName: string;
}

interface ParticipantFormMethods {
    setStartNumber: (value: string) => void,
    setLicensePlate: (value: string) => void,
    setDistance: (value: number) => void,
    setSpeed: (value: number) => void,
    setSessionName: (value: string) => void
}


export const useParticipantForm = create<ParticipantFormProps & ParticipantFormMethods>((set) => ({
    startNumber: "",
    licensePlate: "",
    distance: 0,
    speed: 0,
    sessionName: "",
    setLicensePlate: (value: string) => {
        set({ licensePlate: value })
    },
    setStartNumber: (value: string) => {
        set({ startNumber: value })
    },
    setDistance: (value: number) => {
        set({ distance: value })
    },
    setSpeed: (value: number) => {
        set({ speed: value })
    },
    setSessionName: (value: string) => {
        set({ sessionName: value })
    }
}))
