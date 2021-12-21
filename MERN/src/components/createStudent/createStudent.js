import * as React from 'react';
import {useState} from 'react';
import Box from '@mui/material/Box';
import TextField from '@mui/material/TextField';
import Button from '@mui/material/Button';
import axios from 'axios';

//createStudent doesn't work. First letter needs to be in upperletter
export default function CreateStudent() {
  //useState=react hook
  //updates data in front end.
  const [student,setStudent]=useState({
    regNo:0,
    studentName:'',
    grade:'',
    section:''
  });
  const createStudent=()=>{
    axios.post('http://localhost:3000/students',student).then(()=>{
      window.location.reload(false); //automatically reload when new data
    })
  };

  return (
    <>
    <h2>Create Student</h2>
    <Box
      component="form"
      sx={{
        '& > :not(style)': { m: 1, width: '25ch' },
      }}
      noValidate
      autoComplete="off"
    >
      <TextField id="outlined-basic" label="Registration No" variant="outlined" value={student.regNo} onChange={(event)=>{
        setStudent({...student,regNo:event.target.value})
      }} />
      <TextField id="outlined-basic" label="Name" variant="outlined" value={student.studentName}  onChange={(event)=>{
        setStudent({...student,studentName:event.target.value})
      }} />
      <TextField id="outlined-basic" label="Grade" variant="outlined" value={student.grade}  onChange={(event)=>{
        setStudent({...student,grade:event.target.value})
      }} />
      <TextField id="outlined-basic" label="Section" variant="outlined" value={student.section}  onChange={(event)=>{
        setStudent({...student,section:event.target.value})
      }}  />

      <Button variant="contained" color="primary" onClick={createStudent}>
        Create
      </Button>
    </Box>
    </>
  );
}
