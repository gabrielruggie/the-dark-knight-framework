import './App.css';
import NavBar from './components/NavBar';
import ScheduledGame from './components/ScheduledGame';

export default function Schedule() {
  return (
    
    <div className='bg-white'>

      <div className='grid grid-cols-1'>

        <div>
          <NavBar />
        </div>

        <div className='text-center p-4 pt-12'>

          <div className='md:text-4xl font-bold pb-4 text-orange-500'>YMBL 2022-2023</div>
          <div className='md:text-4xl font-bold text-orange-500'>Regular Season Schedule</div>

        </div>

        <div className='flex flex-wrap space-y-4 justify-center md:m-10'>
          <ScheduledGame />
          <ScheduledGame />
          <ScheduledGame />
          <ScheduledGame />
          <ScheduledGame />
        </div>

      </div>

    </div>  
    
  );
}