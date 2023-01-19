import axios from 'axios';
import React from 'react';
import { useState, useEffect } from 'react';

/* I think the play is to make this a form and each player have its own states
    Since they will each be a mini form, each player's stats will need to be queried/saved to the database
    This could be very costly as everytime they query update stats, they are sending ~100 queries. We will
    definitely need to continue researching how to improve the software but for the first version, I think
    it will do
 */

/**
 */
export default function Player({player}){
    const [updateStats, setUpdateStats] = useState("");
    
    // Update Player Form Fields
    const [playerNumber, setPlayerNumber] = useState(0);
    const [points, updatePoints] = useState(0);
    const [assists, updateAssists] = useState(0);
    const [rebounds, updateRebounds] = useState(0);
    const [steals, updateSteals] = useState(0);
    const [blocks, updateBlocks] = useState(0);
    const [gamesPlayed, updateGamesPlayed] = useState(0);

    // Response Errors
    const [Error, setError] = useState("");

    async function uploadAndDisableEditing (event) {
        event.preventDefault();

        setUpdateStats("disabled");
        await axios.post('https://ymbl-query-backend-3jcqeir73q-uc.a.run.app/ymbl/sendstats', {
          'first_name': player['first_name'],
          'last_name': player['last_name'],
          'email': "",
          'position': "",
          'player_number': parseInt(playerNumber),
          'grade': 0,
          'id': player['id'], // Filled in on backend
          'team_church': player['team_church'],
          'team_cap_name': player['team_cap_name'],
          'team_level': player['team_level'],
          'team_id': player['team_id'],
          'tot_points': player['tot_points'] + parseInt(points),
          'tot_assists': player['tot_assists'] + parseInt(assists),
          'tot_rebounds': player['tot_rebounds'] + parseInt(rebounds),
          'tot_steals': player['tot_steals'] + parseInt(steals),
          'tot_blocks': player['tot_blocks'] + parseInt(blocks),
          'games_played': player['games_played'] + parseInt(gamesPlayed)
        }).then(
          result => {
            window.location.reload();
        })
        .catch(
            err =>{
                console.log(err);
                setUpdateStats("");
                setError(err.response.data);
            });
    }

    const getPlayerFullName = () => {
        return player['first_name'].toUpperCase() + " " + player['last_name'].toUpperCase()
    }

    return (
        <form className='flex justify-between space-x-1 text-orange-500 font-bold m-3 text-center md:p-2 md:text-xl hover:bg-gray-100 hover:rounded-md'>

            <div className='text-red-600 font-bold font-mono text-xl p-1'>{Error}</div>
            <label htmlFor="">{getPlayerFullName()}</label>
            <label htmlFor="">#:</label>
            <input type="text"
            onChange={(event) => setPlayerNumber(event.target.value)}
            className='bg-blue-100 w-10 rounded-md text-gray-500' 
            placeholder={player['player_number']} disabled={updateStats}/>
            <label htmlFor="">Tot. Pts:</label>
            <input type="text" 
            onChange={(event) => updatePoints(event.target.value)}
            className='bg-blue-100 w-10 rounded-md text-gray-500' 
            placeholder={player['tot_points']} disabled={updateStats}/>
            <label htmlFor="">Tot. Asts:</label>
            <input type="text"
            onChange={(event) => updateAssists(event.target.value)}
            className='bg-blue-100 w-10 rounded-md text-gray-500' 
            placeholder={player['tot_assists']} disabled={updateStats}/>
            <label htmlFor="">Tot. Rbds:</label>
            <input type="text" 
            onChange={(event) => updateRebounds(event.target.value)}
            className='bg-blue-100 w-10 rounded-md text-gray-500' 
            placeholder={player['tot_rebounds']} disabled={updateStats}/>
            <label htmlFor="">Tot. Stls:</label>
            <input type="text" 
            onChange={(event) => updateSteals(event.target.value)}
            className='bg-blue-100 w-10 rounded-md text-gray-500' 
            placeholder={player['tot_steals']} disabled={updateStats}/>
            <label htmlFor="">Tot. Blks:</label>
            <input type="text" 
            onChange={(event) => updateBlocks(event.target.value)}
            className='bg-blue-100 w-10 rounded-md text-gray-500' 
            placeholder={player['tot_blocks']} disabled={updateStats}/>
            <label htmlFor="">Tot. GP:</label>
            <input type="text" 
            onChange={(event) => updateGamesPlayed(event.target.value)}
            className='bg-blue-100 w-10 rounded-md text-gray-500'
            placeholder={player['games_played']} disabled={updateStats}/>
            <button className='bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded m-auto' onClick={uploadAndDisableEditing}>
                Update
            </button>

        </form>
    )
}