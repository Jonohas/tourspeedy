import { create } from 'zustand'

interface ParticipantFormProps {
    startNumber: number;
    licensePlate: string;
}

interface ParticipantFormMethods {
    setStartNumber: (value: number) => void,
    setLicensePlate: (value: string) => void,
    clearForm: () => void
}


export const useParticipantForm = create<ParticipantFormProps & ParticipantFormMethods>((set) => ({
    startNumber: 0,
    licensePlate: "",
    setLicensePlate: (value: string) => {
        set({ licensePlate: value })
    },
    setStartNumber: (value: number) => {
        set({ startNumber: value })
    },
    clearForm: () => {
        set({ startNumber: 0, licensePlate: "" })
    }
}))
