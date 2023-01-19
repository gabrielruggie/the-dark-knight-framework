import React from 'react';

export default function Player({player}){
    
    const getPlayerFullName = () => {
        return player['first_name'].toUpperCase() + " " + player['last_name'].toUpperCase()
    }

    const calculateStats = (stat) => {
        return Math.round( (stat/player['games_played'])*100 ) / 100
    }

    return (
        <div className='flex justify-between text-xs space-x-2 text-gray-800 font-bold m-3 text-center md:p-2 md:text-xl hover:bg-amber-100 hover:rounded-md'>
            <div className='flex space-x-3'>
                <div>{getPlayerFullName()}</div>
                <div>#{player['player_number']}</div>
            </div>
            <div>{calculateStats(player['tot_pts'])} PPG</div>
            <div>{calculateStats(player['tot_asts'])} APG</div>
            <div>{player['rpg']} RPG</div>
            <div>{player['spg']} SPG</div>
            <div>{player['bpg']} BPG</div>
            <div>{player['games_played']} GP</div>

        </div>
    )
}