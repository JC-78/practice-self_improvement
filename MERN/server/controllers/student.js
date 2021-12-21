//backend 
import StudentData from '../models/student.js';

export const getStudents=async (req,res)=>{
    try{
        //gets all students in schema
        //wrote async above cuz we use await below
        //we use await because getting all studnets might take a while
    
        const allStudents=await StudentData.find();
        res.status(200).json(allStudents);
        //200 indicates okay. 
        //json(allStudents) moves data in JSON format and no need for conversion.So fast  
    } catch(error){
        //404 indicates not found. http status code 
        res.status(404).json({message:error.message})

    }
}

export const createStudent=async (req,res)=>{
    const student=req.body;
    const newStudent=new StudentData(student);
    //coincidence that model and variable same name
    try{
        await newStudent.save();
        //http status for created
        res.status(201).json(newStudent);
    }catch(error){
        //http status for conflict
        res.status(409).json({message:error.message});
    }
}
//backend 
export const deleteStudent=async (req,res)=>{
    const id=req.params.id;
    try{
        await StudentData.findByIdAndRemove(id).exec();
        res.send('Successfully Deleted!');
    }catch(error){
        console.log(error);
    }
}
