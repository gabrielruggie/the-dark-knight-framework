import React from 'react'

export default function NavBar() {

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
            <div className="hidden md:flex justify-center p-5 bg-gray-800">
                <ul className="flex font-bold text-xl space-x-16">
                    <li className="mr-6">
                        <a className="text-orange-500 hover:text-orange-600" href="#">Home</a>
                    </li>
                    <li className="mr-6">
                        <a className="text-orange-500 hover:text-orange-600" href="#">Register</a>
                    </li>
                    <li className="mr-6">
                        <a className="text-orange-500 hover:text-orange-600" href="#">Standings</a>
                    </li>
                    <li className="mr-6">
                        <a className="text-orange-500 hover:text-orange-600" href="#">Schedule</a>
                    </li>
                    <li className="mr-6">
                        <a className="text-orange-500 hover:text-orange-600" href="#">Stats</a>
                    </li>
                    <li className="mr-6">
                        <a className="text-orange-500 hover:text-orange-600" href="#">Login</a>
                    </li>
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
                        <a href="#" className="block text-md px-2 py-4 text-orange-500 hover:bg-gray-100 font-bold">Home</a>
                    </li>
                    <li className="">
                        <a href="#" className="block text-md px-2 py-4 text-orange-500 hover:bg-gray-100 font-bold">Register</a>
                    </li>
                    <li className="">
                        <a href="#" className="block text-md px-2 py-4 text-orange-500 hover:bg-gray-100 font-bold">Standings</a>
                    </li>
                    <li className="">
                        <a href="#" className="block text-md px-2 py-4 text-orange-500 hover:bg-gray-100 font-bold">Schedule</a>
                    </li>
                    <li className="">
                        <a href="#" className="block text-md px-2 py-4 text-orange-500 hover:bg-gray-100 font-bold">Stats</a>
                    </li>
                    <li className="">
                        <a href="#" className="block text-md px-2 py-4 text-orange-500 hover:bg-gray-100 font-bold">Login</a>
                    </li>
                </ul>
            </div>
        </nav>
    )
}