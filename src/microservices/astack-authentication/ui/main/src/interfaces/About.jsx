import React from 'react'
import { useState, useEffect } from 'react';
import NavBar from './components/NavBar'

export default function About() {
    const [cloudClicked, setCloudClicked] = useState(false);

    const changeCloudState = () => {
        setCloudClicked(true)
    }

    const version = '1.0.1'
    return(
        <div className='bg-black pb-32'>

            <div>
                <NavBar/>
            </div>

            <div className='font-bold text-orange-400 p-12 text-4xl'>
                Admin Stack Beta v{version}
                <div className='text-2xl text-white pt-4'>
                    Learn about what's behind the scenes of the digital infrastructure that powers the YMBL
                </div>

                <div className='pt-20 flex justify-center scale-125'>
                    <img src="https://storage.googleapis.com/ymbl-web-images/ASTACK_BETA_LOGO.png" alt="" />
                </div>
                <div className='pt-20 flex justify-center scale-75'>
                    <img src="https://storage.googleapis.com/ymbl-web-images/STAT_PADDER_V1_0.png" alt="" />
                </div>
            </div>

            <div className='m-20 flex'>
                <aside class="w-64" aria-label="Sidebar">
                    <div class="px-3 py-4 overflow-y-auto rounded-md bg-gray-50 dark:bg-gray-800 text-2xl font-bold">
                        <ul class="space-y-10">
                            <li className='nav-item' role='presentation'>
                                <a onClick={changeCloudState} class="nav-link active flex items-center p-3 text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700">
                                    <span class="ml-3">Google Cloud</span>
                                </a>
                            </li>
                            <li>
                                <a href="#tabs-profile" class="flex items-center p-3 text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700">
                                    <span class="flex-1 ml-3 whitespace-nowrap">Infrastructure</span>
                                </a>
                            </li>
                            <li>
                                <a href="#" class="flex items-center p-3 text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700">
                                    <span class="flex-1 ml-3 whitespace-nowrap">Backend API</span>
                                </a>
                            </li>
                            <li>
                                <a href="#" class="flex items-center p-3 text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700">
                                    <span class="flex-1 ml-3 whitespace-nowrap">Latest Release</span>
                                </a>
                            </li>
                        </ul>
                    </div>
                </aside>
                <div class="ml-10 tab-content text-white" id="tabs-tabContent">
                    <div class={"" + (cloudClicked ? 'block' : 'hidden')} >
                        Tab 1 content
                    </div>
                    <div class="tab-pane fade" id="tabs-profile" role="tabpanel" aria-labelledby="tabs-profile-tab">
                        Tab 2 content
                    </div>
                    <div class="tab-pane fade" id="tabs-messages" role="tabpanel" aria-labelledby="tabs-profile-tab">
                        Tab 3 content
                    </div>
                    <div class="tab-pane fade" id="tabs-contact" role="tabpanel" aria-labelledby="tabs-contact-tab">
                        Tab 4 content
                    </div>
                </div>
            </div>

        </div>
    )
}