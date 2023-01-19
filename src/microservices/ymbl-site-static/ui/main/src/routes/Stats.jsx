import axios from 'axios'
import './App.css';
import NavBar from './components/NavBar';
import TeamList from './components/TeamList';
import React, { useEffect, useState } from 'react'

export default function Stats() {
  const [teamMap, setTeamMap] = useState([]);

  useEffect(

    () => {
      const onLoad = async () => {
        axios({
          method: "GET",
          url: "https://ymbl-query-backend-3jcqeir73q-uc.a.run.app/ymbl/stats"
        }).then(
          result => {
            let data = sortPlayerData(result.data);
            setTeamMap(Object.values(data));

          }).catch();
            // const test_players = [{'first_name':'Gabriel', 'last_name':'Ruggie', 'player_number':12, 'team_id':3902, 'team_church':"St.Luke", 'team_cap_name':'Crilly', 'team_level':4, 'tot_pts':20, 'tot_asts':6, 'games_played':3}, {'first_name':'Daniel', 'last_name':'Ruggie', 'player_number':11, 'team_id':3902, 'team_church':"St.Luke", 'team_cap_name':'Crilly', 'team_level':4}, {'first_name':'Ethan', 'last_name':'Fenlon', 'player_number':3, 'team_id':3902, 'team_church':"St.Luke", 'team_cap_name':'Crilly', 'team_level':4}]
            // console.log(test_players);
            // let data = sortPlayerData(test_players);

            // console.log(Object.values(data));
            // setTeamMap(Object.values(data));
      }
      onLoad()
    }, []

  )

  /**
   * Sorts large player object array into a sorted hash table
   * Keys -> team_id found in player meta data
   * Value -> respective player data
   */
  function sortPlayerData (data) {

    let dataSortedByTeamName = {};

    for (let i = 0; i < data.length; i++){
      let player = data[i];
      // Sort by team id so we can just use the values of this object without ignoring valuable data such as the full team name
      let teamId = player['team_id']
      
      if (!dataSortedByTeamName[teamId]){
        dataSortedByTeamName[teamId] = [player];
      } else {
        dataSortedByTeamName[teamId].push(player);
      }
      
    }
    
    return dataSortedByTeamName;
    
  }

  return (
    
    <div className='bg-white'>

      <div className='grid grid-cols-1'>

        <div>
          <NavBar />
        </div>

        <div className='text-center p-4 pt-12'>

          <div className='md:text-4xl font-bold pb-2 text-orange-500'>YMBL 2022-2023</div>
          <div className='md:text-4xl font-bold text-orange-500'>Player Stats</div>

        </div>

        <div className='md:m-10 space-y-4'>
          <TeamList teamMap={teamMap}/>
        </div>

      </div>

    </div>  
    
  );
}