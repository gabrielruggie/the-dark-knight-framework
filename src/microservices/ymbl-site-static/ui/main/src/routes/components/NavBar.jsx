import React from 'react'
import { useNavigate } from 'react-router-dom'

export default function NavBar() {

    const nav = useNavigate();
    async function renderStatsPage(event) {
        event.preventDefault();
        nav("/stats");

    }
    async function renderSchedulePage(event) {
        event.preventDefault();
        nav("/schedule");

    }
    async function renderAboutPage(event) {
        event.preventDefault();
        nav("/about");
    }
    async function renderHomePage(event) {
        event.preventDefault();
        nav("/");
    }

    async function openMobileNavigation() {
        const mobileMenuBtn = document.querySelector("button.mobile-menu-button");
        const mobileNavBar = document.querySelector(".mobile-menu");

        mobileMenuBtn.addEventListener("click", () => {
            mobileNavBar.classList.toggle("hidden")
        })
    }
    // We should make the href tags have the actual link, served through environment variables 
    // We will need to configure CORS in the api gateway so it can accept requests from this service
    return (
        <nav>
            <div className="hidden md:flex justify-center p-5 bg-gray-800 pb-12 pt-7">
                <ul className="flex font-bold text-3xl space-x-16">
                    <li className="mr-6">
                        <a className="text-orange-500 hover:text-orange-600 cursor-pointer" onClick={renderHomePage}>Home</a>
                    </li>
                    {/* <li className="mr-6">
                        <a className="text-orange-500 hover:text-orange-600 cursor-pointer" onClick={renderRegistrationPage}>Register</a>
                    </li> */}
                    <li className="mr-6">
                        <a className="text-orange-500 hover:text-orange-600 cursor-pointer" onClick={renderSchedulePage}>Schedule</a>
                    </li>
                    <li className="mr-6">
                        <a className="text-orange-500 hover:text-orange-600" onClick={renderStatsPage}>Stats</a>
                    </li>
                    <li className="mr-6">
                        <a className="text-orange-500 hover:text-orange-600 cursor-pointer" onClick={renderAboutPage}>About</a>
                    </li>
                    {/* <li className="mr-6">
                        <a className="text-orange-500 hover:text-orange-600" href="#">Standings</a>
                    </li>
                    <li className="mr-6">
                        <a className="text-orange-500 hover:text-orange-600" href="#">Schedule</a>
                    </li>
                    <li className="mr-6">
                        <a className="text-orange-500 hover:text-orange-600" href="#">Login</a>
                    </li> */}
                </ul>
            </div>
            <div className="md:hidden flex items-center bg-gray-800">
                <button className="outline-none mobile-menu-button" onClick={openMobileNavigation}>
                    <svg
                        className="w-8 h-8 text-white"
                        x-show="!showMenu"
                        fill="none"
                        strokeLinecap="round"
                        strokeLinejoin="round"
                        strokeWidth="2"
                        viewBox="0 0 24 24"
                        stroke="currentColor"
                    >
                    <path d="M4 6h16M4 12h16M4 18h16"></path>
                    </svg>
                </button>
            </div>
            <div className="hidden mobile-menu bg-gray-800">
                <ul className="">
                    <li className="">
                        <a onClick={renderHomePage} className="block text-md px-2 py-4 text-orange-500 hover:bg-gray-100 font-bold">Home</a>
                    </li>
                    <li className="">
                        <a onClick={renderStatsPage} className="block text-md px-2 py-4 text-orange-500 hover:bg-gray-100 font-bold">Stats</a>
                    </li>
                    {/* <li className="">
                        <a onClick={renderRegistrationPage} className="block text-md px-2 py-4 text-orange-500 hover:bg-gray-100 font-bold">Register</a>
                    </li> */}
                    <li className="">
                        <a onClick={renderSchedulePage} className="block text-md px-2 py-4 text-orange-500 hover:bg-gray-100 font-bold">Schedule</a>
                    </li>
                    <li className="">
                        <a onClick={renderAboutPage} className="block text-md px-2 py-4 text-orange-500 hover:bg-gray-100 font-bold">About</a>
                    </li>
                    {/* <li className="">
                        <a href="#" className="block text-md px-2 py-4 text-orange-500 hover:bg-gray-100 font-bold">Standings</a>
                    </li>
                    <li className="">
                        <a href="#" className="block text-md px-2 py-4 text-orange-500 hover:bg-gray-100 font-bold">Schedule</a>
                    </li>
                    <li className="">
                        <a href="#" className="block text-md px-2 py-4 text-orange-500 hover:bg-gray-100 font-bold">Login</a>
                    </li> */}
                </ul>
            </div>
        </nav>
    )
}
