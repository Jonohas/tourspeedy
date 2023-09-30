import { useEffect, useState } from "react";

interface Props {
    start: number | null;
    end: number | null;
    timestamp: number | null;
}

export const Timer = ({start, end, timestamp}: Props) => {

    
	const [timer, setTimer] = useState<string>("");

	function millisecondsSince() {
        let millisecondsPassed = 0;
        if (timestamp && start) {
            millisecondsPassed = timestamp - start;
        }
		return Math.round(millisecondsPassed * 10000) / 10000;
	}

    function finalDiff() {
        let millisecondsPassed = 0;
        if (start && end) {
            millisecondsPassed = end - start;
        }
        return Math.round(millisecondsPassed * 10000) / 10000;
    }

	useEffect(() => {

        if (start) {
            setTimer(`${millisecondsSince()}`)
        }


	}, [timestamp])

	useEffect(() => {
        setTimer(`${finalDiff()}`)
	}, [end])

    return <span>{timer}</span>
};
