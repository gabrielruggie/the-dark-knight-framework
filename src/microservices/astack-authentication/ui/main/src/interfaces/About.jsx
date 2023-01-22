import React from 'react'
import { useState, useEffect } from 'react';
import NavBar from './components/NavBar'

export default function About() {
    const [techClicked, setTechClicked] = useState(false);
    const [infraClicked, setInfraClicked] = useState(false);
    const [apiClicked, setApiClicked] = useState(false);
    const [releaseClicked, setReleaseClicked] = useState(false);


    const changeCloudState = () => {
        setTechClicked(!techClicked);
        setInfraClicked(false);
        setApiClicked(false);
        setReleaseClicked(false);
    }


    const changeInfraClicked = () => {
        setTechClicked(false);
        setInfraClicked(!infraClicked);
        setApiClicked(false);
        setReleaseClicked(false);
    }


    const changeApiClicked = () => {
        setTechClicked(false);
        setInfraClicked(false);
        setApiClicked(!apiClicked);
        setReleaseClicked(false);
    }


    const changeReleaseClicked = () => {
        setTechClicked(false);
        setInfraClicked(false);
        setApiClicked(false);
        setReleaseClicked(!releaseClicked);
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
                    <div class="px-3 py-4 overflow-y-auto rounded-md bg-gradient-to-b from-fuchsia-600 to-fuchsia-900 text-2xl font-bold">
                        <ul class="space-y-12">
                            <li className='nav-item' role='presentation'>
                                <a onClick={changeCloudState} class="nav-link active flex items-center p-3 rounded-lg text-white hover:bg-gray-900">
                                    <span class="ml-3">Tech Stack</span>
                                </a>
                            </li>
                            <li>
                                <a onClick={changeInfraClicked} class="flex items-center p-3 rounded-lg text-white hover:bg-gray-900">
                                    <span class="flex-1 ml-3 whitespace-nowrap">Infrastructure</span>
                                </a>
                            </li>
                            <li>
                                <a onClick={changeApiClicked} class="flex items-center p-3 rounded-lg text-white hover:bg-gray-900">
                                    <span class="flex-1 ml-3 whitespace-nowrap">Backend API</span>
                                </a>
                            </li>
                            <li>
                                <a onClick={changeReleaseClicked} class="flex items-center p-3 rounded-lg text-white hover:bg-gray-900">
                                    <span class="flex-1 ml-3 whitespace-nowrap">Latest Release</span>
                                </a>
                            </li>
                        </ul>
                    </div>
                </aside>
                <div class="ml-10 tab-content text-white" id="tabs-tabContent">
                    <div class={techClicked ? 'p-10 rounded-lg block bg-gradient-to-b from-fuchsia-600 to-fuchsia-900' : 'hidden'} >
                        <span className='font-bold text-4xl underline'>Core</span>
                        <div className='grid grid-cols-2 grid-rows-2'>
                            <div className='m-1 row-span-1 col-span-1 space-y-4'>
                                <div className='font-bold text-2xl'>Terraform</div>
                                <div className='font-bold text-md'>Although the infrastructure of ASTACK Beta is fairly basic, we see the value in learning Infrastructure-As-Code to 
                                    deploy our resources to Google Cloud. As our framework expands, we will begin to reap the benefits of IAC. Currently, 
                                    ASTACK uses Terraform to deploy a couple test and beta databases to Google Cloud and we hope that support for deploying cloud run 
                                    containers is imminent
                                </div>
                                <ul className='p-2 font-mono bg-black rounded-md'>
                                    <li>ymblastack-admin1 demo$ terraform init</li>
                                    <li className='text-white font-bold'>Initializing the backend...</li>
                                    <li className='font-bold text-lime-500'>Terraform has been successfully initialized!</li>
                                </ul>
                            </div>
                            <div className='m-1 row-span-1 col-span-1'>
                                <div className='font-bold text-2xl'>React</div>
                            </div>
                            <div className='m-1 row-span-1 col-span-1'>
                                <div className='font-bold text-2xl'>FastAPI</div>
                            </div>
                            <div className='m-1 row-span-1 col-span-1'>
                                <div className='font-bold text-2xl'>PostgresSQL</div>
                            </div>

                        </div>
                    </div>
                    <div class={infraClicked ? 'block' : 'hidden'}>
                        Tab 2 content
                    </div>
                    <div class={apiClicked ? 'block' : 'hidden'}>
                        Tab 3 content
                    </div>
                    <div class={releaseClicked ? 'block' : 'hidden'}>
                        Tab 4 content
                    </div>
                </div>
            </div>

        </div>
    )
}