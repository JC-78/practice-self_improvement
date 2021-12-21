import express from 'express';
import {getStudents,createStudent,deleteStudent} from '../controllers/student.js'
import student from '../models/student.js';

const router=express.Router();

//req=request,res=response
router.get('/',getStudents);
router.post('/',createStudent);
router.delete('/:id',deleteStudent);

export default router;
