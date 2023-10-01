/*
  This example requires some changes to your config:
  
  ```
  // tailwind.config.js
  module.exports = {
    // ...
    plugins: [
      // ...
      require('@tailwindcss/forms'),
    ],
  }
  ```
*/

import { twMerge } from 'tailwind-merge'

interface Props {
    name: string;
    label: string;
    value?: string | number;
    type?: "number" | "text";
    change: (event: any) => void;
    register: any;
    className?: string
}

export const CustomInput = ({name, label, value, type = "text", change, register, className}: Props) => {
    return (
      <div className="">
        <label htmlFor={name} className="block text-sm font-medium leading-6 text-gray-900">
          {label}
        </label>
        <div className="mt-2">
          <input
            {...register(name, type === "number" ? {
                setValueAs: (value: string) => Number(value),
            } : {})}
            onChange={change}
            type={type}
            name={name}
            id={name}
            defaultValue={value}
            className={twMerge("block w-full rounded-md border-0 py-1.5 px-3 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6", className)}
          />
        </div>
      </div>
    )
  }
  