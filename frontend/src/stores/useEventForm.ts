import { create } from 'zustand'

interface EventFormProps {
    distance: number;
    speed: number;
    sessionName: string;
}

interface EventFormMethods {

    setDistance: (value: number) => void,
    setSpeed: (value: number) => void,
    setSessionName: (value: string) => void
}


export const useEventForm = create<EventFormProps & EventFormMethods>((set) => ({

    distance: 0,
    speed: 0,
    sessionName: "",

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
