import React from 'react'
import { useState, useEffect } from 'react';
import { useNavigate } from "react-router-dom";
import axios from 'axios'

export default function AHome() {
    const [firstname, setFirstname] = useState("");
    const nav = useNavigate();

    useEffect(()=>{
        const onLoad = async() => {
            axios({
                method: "GET",
                url: "https://astack-authenticator-3jcqeir73q-uc.a.run.app/admin-stack/beta-v1.0/oauth/authenticator/verify-astack-admin-token",
                headers: {
                    Authorization: "bearer "+localStorage.getItem("token")
                }
            }).then(
                result => {
                    setFirstname(result.data['username']);
                    
                }).catch(
                    () => {
                        localStorage.removeItem("token");
                        nav("/login", {replace: true});
                }
                )
            }
            onLoad()
        },[]
    )

    const navStatPadder = () => {
        nav("/statpadder", {replace: true});
    }
    
    return (
        <div className='bg-gray-800'>

            <div className='col-span-2 font-bold p-4 space-x-2 justify-items-stretch'>
                <span className='text-xl md:text-3xl text-orange-500 justify-self-center'>ASTACK</span>
                <span className='text-sm md:text-xl text-white text-center'>Beta</span>
            </div>

            <div className='grid grid-cols-2'>

                <div className='flex flex-col pb-80 pt-20'>
                    <div className='pt-20 text-white text-center font-bold text-5xl py-2'> 
                        Welcome, {firstname}
                    </div>

                    <div className='text-white text-center font-bold text-5xl pb-10'>
                        to Admin Stack
                    </div>

                    <div className='text-center text-white text-2xl font-bold pb-32'>
                        See What's New in <span className='text-orange-500'>ASTACK</span> Beta v1.0.1
                    </div>

                    <a href='#news' className='bg-orange-500 hover:bg-orange-600 text-lg font-bold border-b-4 rounded-xl text-white m-auto p-4'>
                        News & Updates
                    </a>
                </div>

                <div className='pt-20 pb-20'>
                    <div className='underline pt-20 text-white text-center font-bold text-6xl pb-4'>
                        Menu
                    </div>

                    <div className= 'pt-8 grid grid-cols-2 text-white hover:text-orange-400 hover:cursor-pointer text-center font-bold text-3xl' onClick={navStatPadder}>
                        <div className='justify-self-end h-20 w-20 mr-4'>
                            <img src="https://storage.googleapis.com/ymbl-web-images/STAT_PADDER_V1_0.png" alt="" />
                        </div>
                        <div className="justify-self-start">
                            Stat Padder
                        </div>
                    </div>

                </div>

            </div>

            <div id='news' className='bg-white text-center pb-32'>

                <div className='pt-32 col-start-3 font-bold text-4xl'>
                    Bringing Church League Basketball Into The Future
                    <div className='text-xl pt-4 text-gray-600'>
                        Introducing ASTACK Beta, the first installment of a software application that will streamline YMBL productivity 10 fold!
                    </div>
                </div>

            </div>

            <div className='grid grid-cols-2 bg-orange-400 pb-24'>
                <div className=" shadow-2xl mt-20 rounded-2xl shadow-gray-800 p-16 justify-center mx-auto">
                    <img src="https://storage.googleapis.com/ymbl-web-images/icons8-google-cloud-240.png" alt="" />
                </div>
                <div className='bg-white p-8 shadow-2xl rounded-md text-left font-bold text-3xl mt-20 mr-10 space-y-4'>
                    <div>Take Control From The Clouds </div>
                    <div className='text-lg text-orange-400 text-left leading-loose'>
                        Deployed as 3 Google Cloud Run Containers and founded on a fast and light weight API, ASTACK Beta is incredibly efficient
                        and highly dependable and responsive. Updates are in the works to improve the request-response cycle and latency, however, 
                        with a microservice architecture, ASTACK Beta v1.0.1 is already up to par and ready to go!
                    </div>
                </div>
            </div>

            <div className='grid grid-rows-3 grid-cols-2 bg-white'>
                <div className='row-span-3 text-left font-bold text-3xl mt-32 ml-10 p-8'>
                    <div className='pb-1'>Quality Is <span className='text-orange-400'> Everything </span></div>
                    <div className='pb-4 text-2xl'>Read What Comes Out Of The Box</div>
                    <div className='text-lg text-orange-400'>
                        <ul className='list-disc space-y-4 pl-4'>
                            <li>Solid performance, founded on FastAPI's speedy API framework</li>
                            <li>Highly dependable authentication service, personalized to ASTACK Beta's admins</li>
                            <li>High availability due to Google Cloud's container orchestration</li>
                            <li>Great abstraction in order to maintain a top user experience</li>
                        </ul>
                    </div>
                </div>
                <div className="justify-self-center scale-125 row-span-1 row-start-2 col-start-2 ">
                    <img src="https://storage.googleapis.com/ymbl-web-images/ASTACK_BETA_LOGO.png" alt="" />
                </div>
            </div>

            <div className='grid grid-rows-3 grid-cols-2 bg-white pb-32 gap-8'>
                <div className="row-span-1 row-start-2 justify-self-center rounded-lg scale-150">
                    <img src="https://storage.googleapis.com/ymbl-web-images/STAT_PADDER_V1_0.png" alt="" />
                </div>
                <div className='bg-white p-8 text-left font-bold text-3xl mt-20 mr-10 pb-2 row-span-3'>
                    <div clas>Introducing <span className='text-orange-400'>ASTACK</span> Stat Padder</div>
                    <div className='pb-4 text-2xl'>The YMBL Statistic Software</div>
                    <div className='text-lg text-orange-400'>
                        <ul className='list-disc space-y-4 pl-4'>
                            <li>Stat Padder v1.1 comes ready to go out of the box</li>
                            <li>Create Teams and add players to start stat padding, view your changes in real time!</li>
                            <li>
                                The point of ASTACK Beta is to be tied to the Youth Ministry Basketball website, and that 
                                stays true with Stat Padder. Stat changes can be seen almost instantly on the YMBL website
                            </li>
                            <li>Updates will continue to roll out in order to upgrade its backend communication and its user interface</li>
                        </ul>
                    </div>
                </div>
            </div>

        </div>
    )
}