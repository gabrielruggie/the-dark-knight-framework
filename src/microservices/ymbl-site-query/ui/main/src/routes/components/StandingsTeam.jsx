import React, { useEffect, useState } from "react";

export default function StandingsTeam({team}){

    const getTeamName = () => {
        return team['church'].toUpperCase() + " " + returnTeamLevelAsString(team['school_level']).toUpperCase() + " " + team['cap_last_name'].toUpperCase();
    }

    const getTeamRecord = () => {
        return team['wins'] + " - " + team['losses'];
    }

    /**
     * Returns the value of `team_level` in the player metadata to the corresponding value 
     */
    function returnTeamLevelAsString (teamLevelNumber) {
        let teamLevels = {
        1:"frosh",
        2:"soph",
        3:"junior",
        4:"senior"
        };

        return teamLevels[teamLevelNumber];

    }

    return (
        <div className="flex space-x-6 md:space-x-24 md:px-36 p-8 text-orange-500 md:text-3xl font-bold bottom-2 hover:bg-gray-100">

            <div>{team['rank']}.</div>
            <div>{getTeamName()}</div>
            <div>{getTeamRecord()}</div>

        </div>
    )
}