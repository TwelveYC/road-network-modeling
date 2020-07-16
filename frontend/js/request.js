export default function request(config) {
    return new Promise((resolve, reject) => {
        const instance = new XMLHttpRequest();
        instance.open(config.method, config.url);
        instance.send()
        instance.onload = function () {
            resolve(JSON.parse(this.responseText));
        }
    })
}