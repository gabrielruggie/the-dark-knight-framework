import React from 'react';
import ReactDOM from 'react-dom/client';
import {BrowserRouter, Route, Routes} from "react-router-dom"
import Home from './routes/Home';
import About from './routes/About';
import Stats from './routes/Stats';
// import LoadStats from './routes/LoadStat'
import Schedule from './routes/Schedule'

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <BrowserRouter>
    <Routes>
      <Route path='/' element={<Home/>} />
      <Route path='/about' element={<About/>} />
      <Route path='/schedule' element={<Schedule/>} />
      <Route path='/stats' element={<Stats/>} />
      {/* <Route path='/stats' element={<LoadStats/>} /> */}
    </Routes>
  </BrowserRouter>

);