import express from 'express';
import bodyParser from 'body-parser';
import mongoose from 'mongoose';
import cors from 'cors';
import studentRoutes from './routes/student.js';

const app=express();

app.use(cors());

app.use(bodyParser.json({limit:"20mb",extend:true}))
app.use(bodyParser.urlencoded({limit:"20mb",extend:true}))
//first parameter: path to all routes for students
app.use('/students',studentRoutes);


const CONNECTION_URL="mongodb+srv://meow:meow78@cluster0.bakce.mongodb.net/myFirstDatabase?retryWrites=true&w=majority";

//try 8000 when it doesn't work
const PORT=process.env.PORT || 3000;

mongoose.connect(CONNECTION_URL,{
    useNewUrlParser:true,useUnifiedTopology:true
}).then(()=>app.listen(PORT,()=>
console.log('connection is established and running on port')
)).catch((err)=>console.log(err.message));

//to avoid warnings in console
//mongoose.set('useFindAndModify',false);  
//all we need to connect to mongodb 
