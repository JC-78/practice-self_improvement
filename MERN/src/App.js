import logo from './logo.svg';
import {container,AppBar,Typography,Grow,Grid, Container} from '@material-ui/core';
//above is from npm install @material-ui/core
//react components that have already been created. No need to recreate the wheel
import Student from './components/showStudent/showStudent.js';
import Create from "./components/createStudent/createStudent";
import './App.css';
import useStyles from './style';



function App() {
  const classes= useStyles();
  return (
    <div className="App">
      <container maxWidth="lg">
        <AppBar className={classes.appBar} position="static" color="inherit"> 
        <Typography className={classes.heading} variant="h2" align="center">Students create & show</Typography>
        </AppBar>

        <Grow in>
          <Container>
            <Grid container justify="space-between" alignItems="strect">
              <Grid item xs={12} sm={7}>
                <AppBar className={classes.appBar} position="static" color="inherit"> </AppBar>
                  <Student />
              </Grid>

              <Grid item xs={12} sm={4}>
                <AppBar className={classes.appBar} position="static" color="inherent">
                  <Create />
                </AppBar>

              </Grid>
            </Grid>
          </Container>
        </Grow>
      </container>
    </div>
  );
}

export default App;
