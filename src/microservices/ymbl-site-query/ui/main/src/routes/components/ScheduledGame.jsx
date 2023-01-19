import React from "react"

export default function ScheduledGame() {
    return (
        <div className="flex justify-between grow md:text-2xl text-white text-center space-x-4 bg-orange-500 hover:bg-orange-600 md:p-4 rounded-md">
            <div>
                <span className="text-gray-200">HOME: </span>
                <span>St. Luke Sr</span>
            </div>
            <div>
                <span className="text-gray-200">AWAY: </span>
                <span>St. Giles Jr</span>
            </div>
            <div>
                <span className="text-gray-200">LOC: </span>
                <span>Ascension</span>
            </div>
            <div>
                <span className="text-gray-200">DATE: </span>
                <span>December 1st, 2022</span>
            </div>
            <div>
                <span className="text-gray-200">TIME: </span>
                <span>10:00 AM</span>
            </div>

        </div>
    )
}