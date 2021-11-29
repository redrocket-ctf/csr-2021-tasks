const ejs = require('ejs')
const fs = require('fs')

// Auto-kill process after some time
setTimeout(() => {
    console.log('Killing child process')
    process.exit()
}, 180000)

isObject = obj => obj && obj.constructor && obj.constructor === Object;

merge = (a, b) => {
    for (let attr in b) {
        if (isObject(a[attr]) && isObject(b[attr])) {
            merge(a[attr], b[attr]);
        } else {
            a[attr] = b[attr];
        }
    }
    return a
}

process.on('message', (message) => {

    let powers = merge(message.state, message.body);
    const data = { powers }

    const str = fs.readFileSync('./views/home.ejs', 'utf8')
    console.log(str.outputFunctionName)
    const template = ejs.compile(str);
    process.send({ html: template({ data }), state: data });

});