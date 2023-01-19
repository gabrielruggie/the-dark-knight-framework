import React from "react";
import NavBar from './components/NavBarHome';
import './App.css'

export default function Home(){

    return (
        <div className="">
            <div className="">
                <NavBar />
            </div>

            <div className="grid grid-cols-2 justify-items-stretch bg-gradient-to-b from-white to-gray-900 pt-10">

                <div className="lg:pt-10 lg:p-8 lg:text-4xl md:text-3xl font-bold pb-4 text-left">
                    <div className="ml-4 md:ml-20 lg:ml-40 pt-10 md:pt-20 text-black md:space-y-1">
                        <div className="">
                            2023. New Year.
                        </div>
                        <div>
                            New Improvements.
                        </div>
                        <div>
                            Bring on YMBL Admin Stack!
                        </div>
                    </div>
                    <div className="flex md:space-x-4 lg:space-x-8 pt-4 xl:pt-4 lg:pt-4 md:pt-4 md:ml-20 lg:ml-40 md:mb-8">
                        <img src="https://storage.googleapis.com/ymbl-web-images/YMBL_SNAP.PNG" alt="image"/>
                        <img src="https://storage.googleapis.com/ymbl-web-images/YMBL_INSTA.PNG" alt="image" />
                        <img src="https://storage.googleapis.com/ymbl-web-images/YMBL_TWIT.PNG" alt="image" />
                    </div>
                </div>

                <div className="md:pl-10 lg:pl-16 pt-10">
                    <img src="https://storage.googleapis.com/ymbl-web-images/YMBL_LOGO.PNG" alt="image" />
                </div>                

            </div>

            <div className="bg-gray-900 text-white pb-12 md:pb-24">
                <div className="text-lg md:text-4xl lg:text-5xl font-bold text-center pt-16 pb-2">
                    ASTACK. STAT TRACK. ALL NET.
                </div>
                <div className="ml-12 mr-12 text-sm md:ml-0 md:mr-0 md:text-2xl lg:text-3xl font-bold text-center">
                    Introducing ASTACK Beta & ASTACK Beta Stat Padder.
                </div>
            </div>

            <div className="grid grid-cols-2 bg-gray-900">
                <div className="justify-self-center md:justify-self-end rounded-lg shadow-2xl shadow-gray-200 p-4 mr-4 ml-4 md:m-12 lg:mr-28 md:p-10 lg:p-16 -skew-y-12 bg-white">
                    <img src="https://storage.googleapis.com/ymbl-web-images/icons8-google-cloud-240.png" alt="" />
                </div>
                <div className="text-white bg-orange-400 font-bold md: text-2xl lg:text-4xl mr-4 ml-4 lg:m-12 lg:ml-28 lg:mr-48 p-4 md:p-6 lg:p-8 md:m-12 rounded-lg skew-y-12 shadow-gray-200 shadow-2xl">
                    <div className="lg:pb-6 md:pb-4 text-lg md:text-2xl lg:text-4xl">Thank God & GCP!</div>
                    <div className="block md:hidden">
                        What's good 2023?
                    </div>
                    <div className="hidden md:block md:text-xl lg:text-2xl">
                        With a little intelligence and a lot of praying, we are excited to bring you some new improvements this year!
                        Read about them down below!
                    </div>
                </div>
            </div>

            <div className="grid bg-gray-900 pt-8 pb-32 space-y-12">

                <div className="hidden md:grid grid-cols-2 p-10 md:m-16 md:text-4xl font-bold bg-gradient-to-r from-sky-400 to-black rounded-lg text-white">
                    <div className="">
                        <div className="">
                            ASTACK ATTACK
                        </div>
                        <div>
                            -------
                        </div>
                        <div className="text-xl leading-relaxed">
                            Its time to announce the newest innovation of the YMBL. Yea the websites cool but we decided to one-up ourselves
                            and develop a software behind all the magic. Read about the first ASTACK Beta feature, ASTACK Beta 
                            Stat Padder, below!
                        </div>
                    </div>
                    <div className="justify-self-end -translate-x-12">
                        <img src="https://storage.googleapis.com/ymbl-web-images/ASTACK_BETA_LOGO.png" alt="" />
                    </div>
                </div>

                <div className="md:hidden grid grid-rows-2 bg-gradient-to-t from-sky-400 to-black rounded-lg text-white font-bold m-8 p-4 pt-12">
                    <div className="justify-self-center h-40 w-40">
                        <img src="https://storage.googleapis.com/ymbl-web-images/ASTACK_BETA_LOGO.png" alt="" />
                    </div>
                    <div className="text-center">
                        <div className="text-2xl">
                            ASTACK ATTACK
                        </div>
                        <div>
                            ------------
                        </div>
                        <div className="text-sm leading-relaxed text-left">
                            Its time to announce the newest innovation of the YMBL. Yea the websites cool but we decided to one-up ourselves
                            and develop a software behind all the magic. Read about the first ASTACK Beta feature, ASTACK Beta 
                            Stat Padder, below!
                        </div>
                    </div>
                </div>

                <div className="hidden md:grid grid-cols-2 p-10 m-16 text-4xl font-bold bg-gradient-to-r from-orange-600 to-black rounded-lg text-white">
                    <div>
                        <div className="">
                            QUICK. EASY. DEPENDABLE
                        </div>
                        <div>
                            -------
                        </div>
                        <div className="text-xl leading-relaxed">
                            We are making stat padding cool again. With ASTACK Beta Stat Padder, it will be easier than ever to check how your
                            favorite player is doing. Just view the stats page located on our website. 2023 is off to a great start here
                            at the YMBL!
                        </div>
                    </div>
                    <div className="justify-self-end -translate-x-16">
                        <img src="https://storage.googleapis.com/ymbl-web-images/STAT_PADDER_V1_0.png" alt="" />
                    </div>
                </div>

                <div className="md:hidden grid grid-rows-2 bg-gradient-to-t from-orange-600 to-black rounded-lg text-white font-bold m-8 p-4 pt-12">
                    <div className="justify-self-center h-40 w-40">
                        <img src="https://storage.googleapis.com/ymbl-web-images/STAT_PADDER_V1_0.png" alt="" />
                    </div>
                    <div className="text-center">
                        <div className="text-2xl">
                            QUICK. EASY. DEPENDABLE
                        </div>
                        <div>
                            -----------------
                        </div>
                        <div className="text-sm leading-relaxed text-left">
                        We are making stat padding cool again. With ASTACK Beta Stat Padder, it will be easier than ever to check how your
                            favorite player is doing. Just view the stats page located on our website. 2023 is off to a great start here
                            at the YMBL!
                        </div>
                    </div>
                </div>

            </div>

        </div>
    )
}