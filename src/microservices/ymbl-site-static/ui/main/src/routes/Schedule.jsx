import React from 'react';
import NavBar from './components/NavBar';

export default function About() {

    const teamRecords = {
      "St. Celestine Sr": "(1-1)",
      "St. Giles Sr": "(1-1)",
      "St. Giles Jr": "(2-0)",
      "St. Luke Sr": "(1-1)",
      "St. Luke Jr": "(0-2)",
      "Ascension Jr": "(0-1)",
      "St. Giles Frosh": "(1-0)"
    }

    return (
      <div className="bg-gray-800 pb-1">
      <NavBar />

      <div className="bg-gray-800 text-center font-bold text-orange-500 pb-2 pt-10">
          <div className="text-xl md:text-5xl text-gray-100">
              YMBL Schedule 2022/23
          </div>
      </div>

      <div className="grid grid-cols-4 md:mr-20 m-2 md:ml-20 rounded-md text-left space-y-5">
          
          <div className="col-span-4 lg:col-start-2 lg:col-span-2 text-lg md:text-2xl lg:text-3xl text-orange-500 font-bold md:mb-2 mt-8">
              Week 1: December 11th, 2022
          </div>

          <div className='col-span-4 lg:col-start-2 lg:col-span-2 grid grid-cols-2 border-2 md:border-4 border-gray-200 rounded-md p-4 bg-gray-200'>
              <div className="col-span-1 text-xs md:text-xl text-orange-500 mb-2 font-bold text-left ml-4 mr-4">
                  <div>
                    St. Celestine Sr  <span className='text-gray-400'> {teamRecords["St. Celestine Sr"]} </span>
                  </div>
                  <div>
                    Ascension Jr <span className='text-gray-400'> {teamRecords["Ascension Jr"]} </span>
                  </div>
                  
              </div>
              <div className="col-start-2 col-span-1 grid grid-rows-2 text-sm md:text-xl text-orange-500 font-bold text-left ml-4 mr-4">
                  <div className='text-xs md:text-xl'>
                    Location: St. Luke School
                  </div>
                  <div className='text-xs md:text-xl'>
                    Time: 12 PM
                  </div>
              </div>
          </div>

          <div className='col-span-4 lg:col-start-2 lg:col-span-2 grid grid-cols-2 border-2 md:border-4 border-gray-200 rounded-md p-4 bg-gray-200'>
              <div className="col-span-1 text-xs md:text-xl text-orange-500 mb-2 font-bold text-left ml-4 mr-4">
                  <div>
                    St. Luke Jr <span className='text-gray-400'> {teamRecords["St. Luke Jr"]} </span>
                  </div>
                  <div>
                    St. Giles Sr <span className='text-gray-400'> {teamRecords["St. Giles Sr"]} </span>
                  </div>
                  
              </div>
              <div className="col-start-2 col-span-1 grid grid-rows-2 text-sm md:text-xl text-orange-500 font-bold text-left ml-4 mr-4">
                  <div className='text-xs md:text-xl'>
                    Location: St. Luke School
                  </div>
                  <div className='text-xs md:text-xl'>
                    Time: 1 PM
                  </div>
              </div>
          </div>

          <div className='col-span-4 lg:col-start-2 lg:col-span-2 grid grid-cols-2 border-2 md:border-4 border-gray-200 rounded-md p-4 bg-gray-200'>
              <div className="col-span-1 text-xs md:text-xl text-orange-500 mb-2 font-bold text-left ml-4 mr-4">
                  <div>
                    St. Giles Jr <span className='text-gray-400'> {teamRecords["St. Giles Jr"]} </span>
                  </div>
                  <div>
                    St. Luke Sr <span className='text-gray-400'> {teamRecords["St. Luke Sr"]} </span>
                  </div>
                  
              </div>
              <div className="col-start-2 col-span-1 grid grid-rows-2 text-sm md:text-xl text-orange-500 font-bold text-left ml-4 mr-4">
                  <div className='text-xs md:text-xl'>
                    Location: St. Luke School
                  </div>
                  <div className='text-xs md:text-xl'>
                    Time: 2 PM
                  </div>
              </div>
          </div>

      </div>   

      <div className="grid grid-cols-4 md:mr-20 m-2 md:ml-20 rounded-md text-left space-y-5">
          
          <div className="col-span-4 lg:col-start-2 lg:col-span-2 text-lg md:text-2xl lg:text-3xl text-orange-500 font-bold md:mb-2 mt-8">
              Week 2: January 8th, 2023
          </div>

          <div className='col-span-4 lg:col-start-2 lg:col-span-2 grid grid-cols-2 border-2 md:border-4 border-gray-200 rounded-md p-4 bg-gray-200'>
              <div className="col-span-1 text-xs md:text-xl text-orange-500 mb-2 font-bold text-left ml-4 mr-4">
                  <div>
                    St. Luke Sr  <span className='text-gray-400'> {teamRecords["St. Luke Sr"]} </span>
                  </div>
                  <div>
                    St. Giles Frosh <span className='text-gray-400'> {teamRecords["St. Giles Frosh"]} </span>
                  </div>
                  
              </div>
              <div className="col-start-2 col-span-1 grid grid-rows-2 text-sm md:text-xl text-orange-500 font-bold text-left ml-4 mr-4">
                  <div className='text-xs md:text-xl'>
                    Location: CANCELLED
                  </div>
                  <div className='text-xs md:text-xl'>
                    Time: CANCELLED
                  </div>
              </div>
          </div>

          <div className='col-span-4 lg:col-start-2 lg:col-span-2 grid grid-cols-2 border-2 md:border-4 border-gray-200 rounded-md p-4 bg-gray-200'>
              <div className="col-span-1 text-xs md:text-xl text-orange-500 mb-2 font-bold text-left ml-4 mr-4">
                  <div>
                    St. Celestine Sr <span className='text-gray-400'> {teamRecords["St. Celestine Sr"]} </span>
                  </div>
                  <div>
                    St. Giles Jr <span className='text-gray-400'> {teamRecords["St. Giles Jr"]} </span>
                  </div>
                  
              </div>
              <div className="col-start-2 col-span-1 grid grid-rows-2 text-sm md:text-xl text-orange-500 font-bold text-left ml-4 mr-4">
                  <div className='text-xs md:text-xl'>
                    Location: CANCELLED
                  </div>
                  <div className='text-xs md:text-xl'>
                    Time: CANCELLED
                  </div>
              </div>
          </div>

          <div className='col-span-4 lg:col-start-2 lg:col-span-2 grid grid-cols-2 border-2 md:border-4 border-gray-200 rounded-md p-4 bg-gray-200'>
              <div className="col-span-1 text-xs md:text-xl text-orange-500 mb-2 font-bold text-left ml-4 mr-4">
                  <div>
                    St. Giles Sr <span className='text-gray-400'> {teamRecords["St. Giles Sr"]} </span>
                  </div>
                  <div>
                    St. Luke Jr <span className='text-gray-400'> {teamRecords["St. Luke Jr"]} </span>
                  </div>
                  
              </div>
              <div className="col-start-2 col-span-1 grid grid-rows-2 text-sm md:text-xl text-orange-500 font-bold text-left ml-4 mr-4">
                  <div className='text-xs md:text-xl'>
                    Location: CANCELLED
                  </div>
                  <div className='text-xs md:text-xl'>
                    Time: CANCELLED
                  </div>
              </div>
          </div>

      </div> 

      <div className="grid grid-cols-4 md:mr-20 m-2 md:ml-20 rounded-md text-left space-y-5">
          
          <div className="col-span-4 lg:col-start-2 lg:col-span-2 text-lg md:text-2xl lg:text-3xl text-orange-500 font-bold md:mb-2 mt-8">
              Week 3: January 14th, 2022
          </div>

          <div className='col-span-4 lg:col-start-2 lg:col-span-2 grid grid-cols-2 border-2 md:border-4 border-gray-200 rounded-md p-4 bg-gray-200'>
              <div className="col-span-1 text-xs md:text-xl text-orange-500 mb-2 font-bold text-left ml-4 mr-4">
                  <div>
                    St. Giles Jr  <span className='text-gray-400'> {teamRecords["St. Giles Jr"]} </span>
                  </div>
                  <div>
                    St. Giles Frosh <span className='text-gray-400'> {teamRecords["St. Giles Frosh"]} </span>
                  </div>
                  
              </div>
              <div className="col-start-2 col-span-1 grid grid-rows-2 text-sm md:text-xl text-orange-500 font-bold text-left ml-4 mr-4">
                  <div className='text-xs md:text-xl'>
                    Location: Ascension
                  </div>
                  <div className='text-xs md:text-xl'>
                    Time: 1:30pm
                  </div>
              </div>
          </div>

          <div className='col-span-4 lg:col-start-2 lg:col-span-2 grid grid-cols-2 border-2 md:border-4 border-gray-200 rounded-md p-4 bg-gray-200'>
              <div className="col-span-1 text-xs md:text-xl text-orange-500 mb-2 font-bold text-left ml-4 mr-4">
                  <div>
                    St. Luke Jr <span className='text-gray-400'> {teamRecords["St. Luke Jr"]} </span>
                  </div>
                  <div>
                    Ascension Jr <span className='text-gray-400'> {teamRecords["Ascension Jr"]} </span>
                  </div>
                  
              </div>
              <div className="col-start-2 col-span-1 grid grid-rows-2 text-sm md:text-xl text-orange-500 font-bold text-left ml-4 mr-4">
                  <div className='text-xs md:text-xl'>
                    Location: Ascension
                  </div>
                  <div className='text-xs md:text-xl'>
                    Time: 2:30pm
                  </div>
              </div>
          </div>

          <div className='col-span-4 lg:col-start-2 lg:col-span-2 grid grid-cols-2 border-2 md:border-4 border-gray-200 rounded-md p-4 bg-gray-200'>
              <div className="col-span-1 text-xs md:text-xl text-orange-500 mb-2 font-bold text-left ml-4 mr-4">
                  <div>
                    St. Giles Sr <span className='text-gray-400'> {teamRecords["St. Giles Sr"]} </span>
                  </div>
                  <div>
                    St. Celestine Sr <span className='text-gray-400'> {teamRecords["St. Celestine Sr"]} </span>
                  </div>
                  
              </div>
              <div className="col-start-2 col-span-1 grid grid-rows-2 text-sm md:text-xl text-orange-500 font-bold text-left ml-4 mr-4">
                  <div className='text-xs md:text-xl'>
                    Location: Ascension
                  </div>
                  <div className='text-xs md:text-xl'>
                    Time: 3:30
                  </div>
              </div>
          </div>

      </div> 

      <div className="grid grid-cols-4 md:mr-20 m-2 md:ml-20 rounded-md text-left space-y-5">
          
          <div className="col-span-4 lg:col-start-2 lg:col-span-2 text-lg md:text-2xl lg:text-3xl text-orange-500 font-bold md:mb-2 mt-8">
              Week 4: January 21st, 2023
          </div>

          <div className='col-span-4 lg:col-start-2 lg:col-span-2 grid grid-cols-2 border-2 md:border-4 border-gray-200 rounded-md p-4 bg-gray-200'>
              <div className="col-span-1 text-xs md:text-xl text-orange-500 mb-2 font-bold text-left ml-4 mr-4">
                  <div>
                    St. Luke Jr  <span className='text-gray-400'> {teamRecords["St. Luke Jr"]} </span>
                  </div>
                  <div>
                    St. Giles Frosh <span className='text-gray-400'> {teamRecords["St. Giles Frosh"]} </span>
                  </div>
                  
              </div>
              <div className="col-start-2 col-span-1 grid grid-rows-2 text-sm md:text-xl text-orange-500 font-bold text-left ml-4 mr-4">
                  <div className='text-xs md:text-xl'>
                    Location: Ascension
                  </div>
                  <div className='text-xs md:text-xl'>
                    Time: 1:30pm
                  </div>
              </div>
          </div>

          <div className='col-span-4 lg:col-start-2 lg:col-span-2 grid grid-cols-2 border-2 md:border-4 border-gray-200 rounded-md p-4 bg-gray-200'>
              <div className="col-span-1 text-xs md:text-xl text-orange-500 mb-2 font-bold text-left ml-4 mr-4">
                  <div>
                    St. Luke Sr <span className='text-gray-400'> {teamRecords["St. Luke Sr"]} </span>
                  </div>
                  <div>
                    St. Celestine Sr <span className='text-gray-400'> {teamRecords["St. Celestine Sr"]} </span>
                  </div>
                  
              </div>
              <div className="col-start-2 col-span-1 grid grid-rows-2 text-sm md:text-xl text-orange-500 font-bold text-left ml-4 mr-4">
                  <div className='text-xs md:text-xl'>
                    Location: Ascension
                  </div>
                  <div className='text-xs md:text-xl'>
                    Time: 2:30pm
                  </div>
              </div>
          </div>

          <div className='col-span-4 lg:col-start-2 lg:col-span-2 grid grid-cols-2 border-2 md:border-4 border-gray-200 rounded-md p-4 bg-gray-200'>
              <div className="col-span-1 text-xs md:text-xl text-orange-500 mb-2 font-bold text-left ml-4 mr-4">
                  <div>
                    Ascension Jr <span className='text-gray-400'> {teamRecords["Ascension Jr"]} </span>
                  </div>
                  <div>
                    St. Giles Jr <span className='text-gray-400'> {teamRecords["St. Giles Jr"]} </span>
                  </div>
                  
              </div>
              <div className="col-start-2 col-span-1 grid grid-rows-2 text-sm md:text-xl text-orange-500 font-bold text-left ml-4 mr-4">
                  <div className='text-xs md:text-xl'>
                    Location: Ascension
                  </div>
                  <div className='text-xs md:text-xl'>
                    Time: 3:30pm
                  </div>
              </div>
          </div>

      </div> 

      <div className="grid grid-cols-4 md:mr-20 m-2 md:ml-20 rounded-md text-left space-y-5">
          
          <div className="col-span-4 lg:col-start-2 lg:col-span-2 text-lg md:text-2xl lg:text-3xl text-orange-500 font-bold md:mb-2 mt-8">
              Week 5: February 5th, 2023
          </div>

          <div className='col-span-4 lg:col-start-2 lg:col-span-2 grid grid-cols-2 border-2 md:border-4 border-gray-200 rounded-md p-4 bg-gray-200'>
              <div className="col-span-1 text-xs md:text-xl text-orange-500 mb-2 font-bold text-left ml-4 mr-4">
                  <div>
                    Ascension Jr  <span className='text-gray-400'> {teamRecords["Ascension Jr"]} </span>
                  </div>
                  <div>
                    St. Luke Jr <span className='text-gray-400'> {teamRecords["St. Luke Jr"]} </span>
                  </div>
                  
              </div>
              <div className="col-start-2 col-span-1 grid grid-rows-2 text-sm md:text-xl text-orange-500 font-bold text-left ml-4 mr-4">
                  <div className='text-xs md:text-xl'>
                    Location: TBD
                  </div>
                  <div className='text-xs md:text-xl'>
                    Time: TBD
                  </div>
              </div>
          </div>

          <div className='col-span-4 lg:col-start-2 lg:col-span-2 grid grid-cols-2 border-2 md:border-4 border-gray-200 rounded-md p-4 bg-gray-200'>
              <div className="col-span-1 text-xs md:text-xl text-orange-500 mb-2 font-bold text-left ml-4 mr-4">
                  <div>
                    St. Luke Sr <span className='text-gray-400'> {teamRecords["St. Luke Sr"]} </span>
                  </div>
                  <div>
                    St. Giles Jr <span className='text-gray-400'> {teamRecords["St. Giles Jr"]} </span>
                  </div>
                  
              </div>
              <div className="col-start-2 col-span-1 grid grid-rows-2 text-sm md:text-xl text-orange-500 font-bold text-left ml-4 mr-4">
                  <div className='text-xs md:text-xl'>
                    Location: TBD
                  </div>
                  <div className='text-xs md:text-xl'>
                    Time: TBD
                  </div>
              </div>
          </div>

          <div className='col-span-4 lg:col-start-2 lg:col-span-2 grid grid-cols-2 border-2 md:border-4 border-gray-200 rounded-md p-4 bg-gray-200'>
              <div className="col-span-1 text-xs md:text-xl text-orange-500 mb-2 font-bold text-left ml-4 mr-4">
                  <div>
                    St. Giles Sr <span className='text-gray-400'> {teamRecords["St. Giles Sr"]} </span>
                  </div>
                  <div>
                    St. Giles Frosh <span className='text-gray-400'> {teamRecords["St. Giles Frosh"]} </span>
                  </div>
                  
              </div>
              <div className="col-start-2 col-span-1 grid grid-rows-2 text-sm md:text-xl text-orange-500 font-bold text-left ml-4 mr-4">
                  <div className='text-xs md:text-xl'>
                    Location: TBD
                  </div>
                  <div className='text-xs md:text-xl'>
                    Time: TBD
                  </div>
              </div>
          </div>

      </div> 

      <div className="grid grid-cols-4 md:mr-20 m-2 md:ml-20 rounded-md text-left space-y-5">
          
          <div className="col-span-4 lg:col-start-2 lg:col-span-2 text-lg md:text-2xl lg:text-3xl text-orange-500 font-bold md:mb-2 mt-8">
              Week 6: February 12th, 2023
          </div>

          <div className='col-span-4 lg:col-start-2 lg:col-span-2 grid grid-cols-2 border-2 md:border-4 border-gray-200 rounded-md p-4 bg-gray-200'>
              <div className="col-span-1 text-xs md:text-xl text-orange-500 mb-2 font-bold text-left ml-4 mr-4">
                  <div>
                    St. Celestine Sr  <span className='text-gray-400'> {teamRecords["St. Celestine Sr"]} </span>
                  </div>
                  <div>
                    St. Giles Frosh <span className='text-gray-400'> {teamRecords["St. Giles Frosh"]} </span>
                  </div>
                  
              </div>
              <div className="col-start-2 col-span-1 grid grid-rows-2 text-sm md:text-xl text-orange-500 font-bold text-left ml-4 mr-4">
                  <div className='text-xs md:text-xl'>
                    Location: St.Luke
                  </div>
                  <div className='text-xs md:text-xl'>
                    Time: 12pm
                  </div>
              </div>
          </div>

          <div className='col-span-4 lg:col-start-2 lg:col-span-2 grid grid-cols-2 border-2 md:border-4 border-gray-200 rounded-md p-4 bg-gray-200'>
              <div className="col-span-1 text-xs md:text-xl text-orange-500 mb-2 font-bold text-left ml-4 mr-4">
                  <div>
                    St. Luke Jr <span className='text-gray-400'> {teamRecords["St. Luke Jr"]} </span>
                  </div>
                  <div>
                    Ascension Jr <span className='text-gray-400'> {teamRecords["Ascension Jr"]} </span>
                  </div>
                  
              </div>
              <div className="col-start-2 col-span-1 grid grid-rows-2 text-sm md:text-xl text-orange-500 font-bold text-left ml-4 mr-4">
                  <div className='text-xs md:text-xl'>
                    Location: St.Luke
                  </div>
                  <div className='text-xs md:text-xl'>
                    Time: 1pm
                  </div>
              </div>
          </div>

          <div className='col-span-4 lg:col-start-2 lg:col-span-2 grid grid-cols-2 border-2 md:border-4 border-gray-200 rounded-md p-4 bg-gray-200'>
              <div className="col-span-1 text-xs md:text-xl text-orange-500 mb-2 font-bold text-left ml-4 mr-4">
                  <div>
                    St. Luke Sr <span className='text-gray-400'> {teamRecords["St. Luke Sr"]} </span>
                  </div>
                  <div>
                    St. Giles Sr <span className='text-gray-400'> {teamRecords["St. Giles Sr"]} </span>
                  </div>
                  
              </div>
              <div className="col-start-2 col-span-1 grid grid-rows-2 text-sm md:text-xl text-orange-500 font-bold text-left ml-4 mr-4">
                  <div className='text-xs md:text-xl'>
                    Location: St.Luke
                  </div>
                  <div className='text-xs md:text-xl'>
                    Time: 2pm
                  </div>
              </div>
          </div>

      </div> 

      <div className="grid grid-cols-4 md:mr-20 m-2 md:ml-20 rounded-md text-left space-y-5">
          
          <div className="col-span-4 lg:col-start-2 lg:col-span-2 text-lg md:text-2xl lg:text-3xl text-orange-500 font-bold md:mb-2 mt-8">
              Week 7: February 19th, 2023
          </div>

          <div className='col-span-4 lg:col-start-2 lg:col-span-2 grid grid-cols-2 border-2 md:border-4 border-gray-200 rounded-md p-4 bg-gray-200'>
              <div className="col-span-1 text-xs md:text-xl text-orange-500 mb-2 font-bold text-left ml-4 mr-4">
                  <div>
                    St. Giles Frosh  <span className='text-gray-400'> {teamRecords["St. Giles Frosh"]} </span>
                  </div>
                  <div>
                    Ascension Jr <span className='text-gray-400'> {teamRecords["Ascension Jr"]} </span>
                  </div>
                  
              </div>
              <div className="col-start-2 col-span-1 grid grid-rows-2 text-sm md:text-xl text-orange-500 font-bold text-left ml-4 mr-4">
                  <div className='text-xs md:text-xl'>
                    Location: St.Luke
                  </div>
                  <div className='text-xs md:text-xl'>
                    Time: 12pm
                  </div>
              </div>
          </div>

          <div className='col-span-4 lg:col-start-2 lg:col-span-2 grid grid-cols-2 border-2 md:border-4 border-gray-200 rounded-md p-4 bg-gray-200'>
              <div className="col-span-1 text-xs md:text-xl text-orange-500 mb-2 font-bold text-left ml-4 mr-4">
                  <div>
                    St. Giles Sr <span className='text-gray-400'> {teamRecords["St. Giles Sr"]} </span>
                  </div>
                  <div>
                    St. Giles Jr <span className='text-gray-400'> {teamRecords["St. Giles Jr"]} </span>
                  </div>
                  
              </div>
              <div className="col-start-2 col-span-1 grid grid-rows-2 text-sm md:text-xl text-orange-500 font-bold text-left ml-4 mr-4">
                  <div className='text-xs md:text-xl'>
                    Location: St.Luke
                  </div>
                  <div className='text-xs md:text-xl'>
                    Time: 1pm
                  </div>
              </div>
          </div>

          <div className='col-span-4 lg:col-start-2 lg:col-span-2 grid grid-cols-2 border-2 md:border-4 border-gray-200 rounded-md p-4 bg-gray-200'>
              <div className="col-span-1 text-xs md:text-xl text-orange-500 mb-2 font-bold text-left ml-4 mr-4">
                  <div>
                    St. Luke Sr <span className='text-gray-400'> {teamRecords["St. Luke Sr"]} </span>
                  </div>
                  <div>
                    St. Celestine Sr <span className='text-gray-400'> {teamRecords["St. Celestine Sr"]} </span>
                  </div>
                  
              </div>
              <div className="col-start-2 col-span-1 grid grid-rows-2 text-sm md:text-xl text-orange-500 font-bold text-left ml-4 mr-4">
                  <div className='text-xs md:text-xl'>
                    Location: St.Luke
                  </div>
                  <div className='text-xs md:text-xl'>
                    Time: 2pm
                  </div>
              </div>
          </div>

      </div> 

      <div className="grid grid-cols-4 md:mr-20 m-2 md:ml-20 rounded-md text-left space-y-5 pb-32">
          
          <div className="col-span-4 lg:col-start-2 lg:col-span-2 text-lg md:text-2xl lg:text-3xl text-orange-500 font-bold md:mb-2 mt-8">
              Week 8: February 26th, 2023
          </div>

          <div className='col-span-4 lg:col-start-2 lg:col-span-2 grid grid-cols-2 border-2 md:border-4 border-blue-400 rounded-md p-4 bg-blue-400'>
              <div className="col-span-1 text-xs md:text-xl text-gray-200 mb-2 font-bold text-left ml-4 mr-4">
                  <div>
                    ALL-YMBL <span className='text-blue-600'>Blue</span>
                  </div>
                  <div>
                    ALL-YMBL <span className='text-red-800'>Red</span>
                  </div>
                  
              </div>
              <div className="col-start-2 col-span-1 grid grid-rows-2 text-sm md:text-xl text-gray-200 font-bold text-left ml-4 mr-4">
                  <div className='text-xs md:text-xl'>
                    Location: St.Luke
                  </div>
                  <div className='text-xs md:text-xl'>
                    Time: 1pm
                  </div>
              </div>
          </div>

      </div> 

  </div>
    )
  }