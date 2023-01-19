import React from 'react';
import ReactDOM from 'react-dom/client';
import {BrowserRouter, Route, Routes} from "react-router-dom"
import Standings from './routes/Standings';
import Stats from './routes/Stats';
import Schedule from './routes/Schedule';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <BrowserRouter>
    <Routes>
      <Route path="/standings" element={<Standings />}/>
      <Route path="/schedule" element={<Schedule />}/>
      <Route path="/stats" element={<Stats />}/>
    </Routes>
  </BrowserRouter>

);
