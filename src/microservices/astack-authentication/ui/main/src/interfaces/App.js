import {BrowserRouter, Route, Routes, useParams} from 'react-router-dom';
import Registration from './Registration';
import Login from './Login';
import AHome from './AHome';
import StatPadder from './StatPadder';
import './App.css';

function App() {
  const {userKey} = useParams();
  return (
    <BrowserRouter>
      <Routes>
        <Route path='registration/:key' element={ <Registration/>} />
        <Route path='login' element={ <Login/>} />
        <Route path='home' element={ <AHome/> } />
        <Route path='statpadder' element={ <StatPadder/> }/>
      </Routes>
  </BrowserRouter>

  );
}

export default App;
