import './App.css';
import NavBar from './components/NavBar';
import React from 'react'

export default function Stats() {

  return (
    
    <div className='bg-white'>

        <div className='grid grid-cols-1'>

            <div>
                <NavBar />
            </div>

            <div className='font-bold text-4xl text-center p-8 lg:p-48 space-y-6'>
                <div>
                    STATS OTW [========={'>'}] 99%
                </div>
                <div>
                    CHECK BACK AFTER WEEK 3!!!
                </div>
            </div>

        </div>

    </div>  
    
  );
}