import React from 'react'
import { useNavigate } from 'react-router-dom'

export default function NavBar() {

    const nav = useNavigate();
    async function renderLogin(event) {
        event.preventDefault();
        nav("/login");
    }

    async function openMobileNavigation() {
        const mobileMenuBtn = document.querySelector("button.mobile-menu-button");
        const mobileNavBar = document.querySelector(".mobile-menu");

        mobileMenuBtn.addEventListener("click", () => {
            mobileNavBar.classList.toggle("hidden")
        })
    }
    return (
        <nav>
            <div className="hidden md:flex justify-left p-5 bg-black pb-12 pt-7">
                <ul className="flex font-bold text-3xl space-x-16">
                    <li className="ml-10 text-white">
                        ASTACK Beta
                    </li>
                    <li className="mr-6">
                        <a className="text-orange-400 hover:text-orange-600 cursor-pointer" onClick={renderLogin}>Login</a>
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
                    <li className="ml-10 text-white">
                        ASTACK Beta
                    </li>
                    <li className="">
                        <a onClick={renderLogin} className="block text-md px-2 py-4 text-orange-500 hover:bg-gray-100 font-bold">Login</a>
                    </li>
                </ul>
            </div>
        </nav>
    )
}
