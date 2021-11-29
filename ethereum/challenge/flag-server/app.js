const createError = require('http-errors')
const express = require('express')
const cors = require('cors')

const indexRouter = require('./routes/index')
const usersRouter = require('./routes/users')
const flagsRouter = require('./routes/flags')

const app = express()

app.use(cors())
app.use(express.json())
app.use(express.urlencoded({ extended: false }))
app.use('/', indexRouter)
app.use('/users', usersRouter)
app.use('/flags', flagsRouter)

// catch 404 and forward to error handler
app.use(function (req, res, next) {
  next(createError(404))
})

// error handler
app.use(function (err, req, res, next) {
  // set locals, only providing error in development
  res.locals.message = err.message
  res.locals.error = req.app.get('env') === 'development' ? err : {}

  // render the error page
  res.status(err.status || 500)
  res.render('error')
})

module.exports = app
