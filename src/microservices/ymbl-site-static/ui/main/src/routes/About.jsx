import React from 'react';
import NavBar from './components/NavBar';

export default function About() {
    return (
      <div>
        <NavBar />

        <div className='grid grid-cols-2 justify-items-stretch place-items-start'>

          <div className="grid grid-rows-5 grid-cols-5 place-items-end  pt-20">
            <img className='row-start-1 row-end-2 col-start-1 col-span-2' src="https://storage.googleapis.com/ymbl-web-images/YMBL_TEAM1_BLK.PNG" alt="" />
            <img className='row-start-2 row-end-3 col-start-2 col-span-2' src="https://storage.googleapis.com/ymbl-web-images/YMBL_TEAM2_BLK.PNG" alt="" />
            <img className='row-start-3 row-end-4 col-start-3 col-span-2' src="https://storage.googleapis.com/ymbl-web-images/YMBL_TEAM3_BLK.PNG" alt="" />
            <img className='row-start-3 row-end-4 col-span-2' src="https://storage.googleapis.com/ymbl-web-images/YMBL_TEAM4_BLK.PNG" alt="" />
            <img className='row-start-1 row-end-2 col-span-2' src="https://storage.googleapis.com/ymbl-web-images/YMBL_TEAM5_BLK.PNG" alt="" />
          </div>

          <div className="grid grid-rows-3 grid-cols-4 pt-10 md:pt-20 font-bold pb-4">
              <div className="text-black col-span-4 xl:col-span-3 xl:col-start-1 md:text-3xl pt-10 text-left">
                The Future of Youth Ministry Basketball and Church League Hoops is Finally Here
              </div>
              <div className="text-gray-500 col-span-4 xl:col-span-3 xl:col-start-1 text-sm md:text-xl text-left pt-6 md:pr-4 lg:pr-24">
                Learn about why should should consider joing our team and our mission.
              </div>
          </div>

          <div className='flex flex-wrap flex-col justify-center font-bold'>
            <div className='text-xl md:text-3xl text-black text-center'>
              Who We Are
            </div>
            <div className='pl-6 pr-6 pt-4 text-sm md:text-xl text-gray-500 md:pl-10 md:pr-10'>
              Youth Ministry Basketball League (YMBL) is a Catholic church-based basketball league for high school boys.
              The league is competitive and structured, but it is intended to be a fun, positive outlet.
            </div>
            <div className='pl-6 pr-6 pt-4 text-sm md:text-xl text-gray-500 md:pl-10 md:pr-10'>
              All boys of high school age are invited whether they are active in a local parish or not.
              No basketball experience is necessary.
            </div>
            <div className='pl-6 pr-6 pt-4 text-sm md:text-xl text-center text-gray-500 md:pl-10 md:pr-10'>
              Read more and consider joining us.
            </div>
          </div>

          <div className='space-y-8 md:pr-12 xl:pr-32'>
            <div className='flex'>
              <img className='pb-36 md:pb-20 pr-2' src="https://storage.googleapis.com/ymbl-web-images/cross-holy-bible-jesus-christian-religious-1-30810.png" alt="cross" />
              <div className='text-md font-bold md:text-xl'>
                Catholic
                <div className='text-xs text-gray-500 md:text-lg'>
                  The mission of the YMBL is to bring high school boys together through basketball and the church. One of our goals for the future is to include a
                  service project as part of the league's scheduled events.
                </div>
              </div>
            </div>
            <div className='flex'>
              <img className='pb-36 md:pb-20 pr-2' src="https://storage.googleapis.com/ymbl-web-images/Black_book_icon.svg.png" alt="" />
              <div className='text-md font-bold md:text-xl'>
                Student Lead
                <div className='text-xs text-gray-500 md:text-lg'>
                  Since its start in 2019, the YMBL has been designed, organized and led by students for students. Adults are present as both practices and games, however
                  the league's season and its future is every player's responsibility.
                </div>
              </div>
            </div>
            <div className='flex'>
              <img className='pb-36 md:pb-28 pr-2' src="https://storage.googleapis.com/ymbl-web-images/basketball-23.png" alt="" />
              <div className='text-md font-bold md:text-xl'>
                Complete Basketball Experience
                <div className='text-xs text-gray-500 md:text-lg'>
                  The YMBL experience includes a regular season of 8 to 10 games, playoff games, official referees, stat updates and a social media presence for players,
                  friends, fans and family.
                </div>
              </div>
            </div>
          </div>
        </div>

      </div>
    )
  }