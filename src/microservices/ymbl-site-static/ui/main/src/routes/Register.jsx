import React from "react";
import NavBar from './components/NavBarHome';
import './App.css'

export default function Register(){

    // Open Team Captain Form
    async function openForm(){
        window.location.href = 'https://docs.google.com/forms/d/e/1FAIpQLSfR1ln7dH4wNpwjX8zLxYpcZmA_DWsvVYLiqPoflqtzmNIFLQ/viewform?usp=sf_link'
    }

    // Open Single Player Registration
    async function singlePlayer() {
        window.location.href = 'https://docs.google.com/forms/d/e/1FAIpQLSfdAb3oNV_YV6pHTFXn-ixmJNP7fQbyviNaNdUfCCtXtV8j8Q/viewform?usp=sf_link'
    }

    return (
        <div className="bg-gray-800 pb-1">
            <NavBar />

            <div className="bg-gray-800 text-center font-bold text-orange-500 pb-2 pt-10">
                <div className="text-xl md:text-5xl text-gray-100">
                    Ready to Join?
                </div>
                <div className="text-sm md:text-2xl m-4 md:m-10 lg:mr-36 lg:ml-36 ">
                    There are two ways to become a member. Register for free today!
                </div>
            </div>

            <div className="grid grid-cols-2 pb-8">
                <div className="bg-gray-800 pt-10 md:pl-20">
                    <img src="https://storage.googleapis.com/ymbl-web-images/YMBL_LOGO.PNG" alt="image" />
                </div>

                <div className="flex flex-col flex-wrap justify-self-center md:mr-20 m-2 md:ml-20 md:mb-20 md:p-4 text-center">
                    <div className="text-md md:text-2xl text-orange-500 font-bold mb-2 lg:mb-8">
                        Full Registration Features
                    </div>
                    <ul className="text-cyan-300 text-xs lg:text-lg font-bold space-y-4">
                        <li>
                            8 Regular Season Games
                        </li>
                        <li>
                            Single Elimination Post Season Tournament
                        </li>
                        <li>
                            Practice Times + Facility at One of Our Sponsoring Parishes
                        </li>
                        <li>
                            Up to Date Player Stat Reporting for Regular Season and Post Season Games
                        </li>
                        <li>
                            Games Officiated by IHSA-Registered Referees
                        </li>
                    </ul>
                </div>
            </div>
            <div className="flex flex-col flex-wrap justify-self-center md:mr-20 m-2 md:ml-20 md:mb-20 md:p-4 rounded-md text-center border-2 md:border-4 border-orange-500">
                <div className="text-lg md:text-2xl lg:text-3xl text-orange-500 font-bold mb-4 md:mb-8 mt-8">
                    Register As A Single Player 
                </div>
                <div className="text-sm md:text-lg text-orange-500 mb-4 md:mb-8 font-bold text-left ml-4 mr-4">
                    Click on the link below to join as a single player on an already established team in our league.
                </div>
                <ul className="text-cyan-300 text-sm md:text-md lg:text-lg font-bold space-y-4 mb-4 text-left ml-6 md:ml-20">
                    <li>
                        Remember to become a completely registered player, you must pay the YMBL League Fee. More information at the bottom of this page
                    </li>
                </ul>
                <button className="text-md text-cyan-300 rounded-md m-10 md:mr-40 md:ml-40 font-bold bg-transparent border-2 border-cyan-300 hover:text-gray-100 hover:border-gray-100" onClick={singlePlayer}>
                    SINGLE PLAYER REGISTRATION HERE
                </button>
            </div>
            <div className="flex flex-col flex-wrap justify-self-center md:mr-20 m-2 md:ml-20 md:mb-20 md:p-4 rounded-md text-center border-2 md:border-4 border-orange-500">
                <div className="text-lg md:text-2xl lg:text-3xl text-orange-500 font-bold mb-4 md:mb-8 mt-8">
                    Team Captain Registration
                </div>
                <div className="text-sm md:text-lg text-orange-500 mb-2 font-bold text-left ml-4 mr-4">
                    Because we want to grow the league, we're offering any one player 25% off your registration if you assemble a new team with us.
                </div>
                <div className="text-sm md:text-lg text-orange-500 mb-2 font-bold text-left ml-6 md:ml-20">
                    Here's what the team captain needs to do:
                </div>
                <ul className="text-cyan-300 text-sm md:text-md lg:text-lg font-bold space-y-1 mb-2 text-left ml-6 md:ml-20 md:mr-20">
                    <li>
                        1. Click on the link below to register as a team captain
                    </li>
                    <li>
                        2. Assemble a team of at least 6 players.
                    </li>
                    <li>
                        3. We'll email you when its time for your players to register.
                    </li>
                    <li>
                        4. When your players are fully registered and paid in full, we'll give you, the team captain, 25% off your registration.
                    </li>
                </ul>
                <div className="text-sm md:text-lg text-orange-500 mb-2 font-bold text-left ml-6 md:ml-20">
                    Remember:
                </div>
                <ul className="text-cyan-300 text-sm md:text-md lg:text-lg font-bold space-y-1 mb-4 text-left ml-6 md:ml-20">
                    <li>
                        - A new team must consist of at least 6 players
                    </li>
                    <li>
                        - All players on a team must be EITHER uppclassmen (juniors or seniors) or underclassmen (freshmen or sophomores).
                    </li>
                    <li>
                        - When your players are fully registered and paid in full, we'll give you, the team captain, 25% off your registration.
                    </li>
                </ul>
                <button className="text-md text-cyan-300 rounded-md m-10 md:mr-40 md:ml-40 font-bold bg-transparent border-2 border-cyan-300 hover:text-gray-100 hover:border-gray-100" onClick={openForm}>
                    TEAM CAPTAINS REGISTER HERE
                </button>
            </div>
            <div className="flex flex-col flex-wrap justify-self-center md:mr-20 mt-8 m-2 md:ml-20 md:mb-20 md:p-4 text-center">
                <div className="text-md md:text-4xl text-orange-500 font-bold md:mb-8 mb-2 lg:mb-8">
                    Becoming A Paid Member (More info coming soon!)
                </div>
                <ul className="text-cyan-300 text-xs md:text-lg font-bold space-y-4 ml-4 mr-4 lg:ml-24 lg:mr-24">
                    <li>
                        In order to become a fully registered player with the YMBL, a one time, non-refundable payment is required
                    </li>
                    <li>
                        This one time payment differs in amount depending on which registration method you choose above. 
                    </li>
                    <li>
                        Once you are registered, check the stats page for your name!
                    </li>
                </ul>
            </div>

        </div>
    )
}