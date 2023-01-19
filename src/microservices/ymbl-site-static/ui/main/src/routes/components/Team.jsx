import React, { useEffect, useState } from "react"
import PlayerList from "./PlayerList";


export default function Team({Team}) {
    const [teamName, setTeamName] = useState("");
    const [playerList, setPlayerList] = useState([]);

    useEffect(
        () => {

            const onLoad = () => {
                setPlayerList(Team);
                let player = Team[0];
                let teamName = player['team_church'].toUpperCase() + " " + returnTeamLevelAsString(player["team_level"]).toUpperCase() + " " + player["team_cap_name"].toUpperCase();
                
                console.log(teamName);
                setTeamName(teamName);
            }
            onLoad();

        },[]
    )

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
    
    // Scrap Standings all together
    return (
        <div className="bg-white border-4 border-orange-500 text-left md:p-3 space-y-2 rounded-md">

            <div className="text-orange-500 font-bold md:text-2xl font-mono">{teamName}</div>
            <div>
                <PlayerList teamPlayers={playerList} />
            </div>

        </div>
    )
}