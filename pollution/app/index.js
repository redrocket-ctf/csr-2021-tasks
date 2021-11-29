const express = require('express');
const bodyParser = require('body-parser')
const cors = require('cors')
const app = express();
const session = require('express-session');
const FileStore = require('session-file-store')(session);
const { fork } = require('child_process');

process.env.NODE_ENV = 'production';

app.set('view engine', 'ejs');
app.use(bodyParser.json())
app.use(bodyParser.urlencoded({
    extended: true
}))
app.use(cors())
app.use(express.static('./public'));

const options = {
    store: new FileStore({
        ttl: 60,
        retries: 1,
        reapInterval: 200
    }),
    secret: 'okspdowe0837pxfimeoiq',
    resave: false,
    unset: "destroy",
    saveUninitialized: false,
    name: 'rumble',
    cookie: {
        // Session expires after 1 min of inactivity.
        expires: 60000
    }
};

app.use(session(options));

const getInitialState = () => {
    const state = {
        powers: {
            inbox: "cleaning. Because storing 60 000 unread emails consumes energy",
            unused: "clothes can be donated or sold to encourage the use of 2nd hand clothes",
            eating: "locally produced food.",
        },
        activatedPowers: []
    }
    state.activatedPowers = Array(Object.keys(state.powers).length).fill(false)

    return state
}

app.get('/', (req, res) => {
    if (req.session.state) res.setHeader('Content-Type', 'text/html');
    else req.session.state = getInitialState()
    res.render('home', { data: req.session.state });
});

app.post('/', (req, res) => {
    if (req.session.state) res.setHeader('Content-Type', 'text/html');
    else req.session.state = getInitialState()

    req.session.child = fork('ejs_compile.js');
    req.session.child.on('message', (message) => {
        req.session.state = message.state
        res.send(message.html);
    });
    req.session.child.send({ state: req.session.state.powers, body: req.body });
});

app.listen(3000, function() {});