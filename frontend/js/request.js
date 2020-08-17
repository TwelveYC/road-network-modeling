import { threadId } from "worker_threads";

export default function request(config) {
    return new Promise((resolve, reject) => {
        const instance = new XMLHttpRequest();
        instance.open(config.method, config.url);
        instance.send();
        instance.onload = function () {
            console.log(this.responseText)
            resolve(JSON.parse(this.responseText));
        }
    })
}