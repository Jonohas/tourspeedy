import { io } from 'socket.io-client';

// "undefined" means the URL will be computed from the `window.location` object
// const URL = process.env.NODE_ENV === 'production' ? undefined : 'http://localhost:8000';
const URL: string = "http://localhost:8000"

export const socket = io(URL, {
    path: "/sockets"
});
