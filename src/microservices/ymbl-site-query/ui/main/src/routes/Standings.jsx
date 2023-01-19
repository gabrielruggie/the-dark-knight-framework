import axios from 'axios'
import { useEffect, useState } from 'react';
import './App.css';
import NavBar from './components/NavBar';
import StandingsTeamList from './components/StandingsTeamList';

export default function Standings() {
  const [teams, setTeams] = useState([]);

  useEffect(
    () => {
      const onLoad = async () => {
        axios({
          method: "GET",
          url: "https://ymbl-query-backend-3jcqeir73q-uc.a.run.app/ymbl/standings"
        }).then(
          result => 
          {
            console.log(sortTeamsByWins(result.data))
            let sortedTeamsData = sortTeamsByWins(result.data);
            let teamsList = addStandingsRankingNumber(sortedTeamsData);
            console.log(teamsList);
            setTeams(sortTeamsByWins(teamsList));
          }
        ).catch();
      }
      onLoad()
    }, []
  )
  
  /**
   * Sorts team data from query by wins
   */
  function sortTeamsByWins (teamsData) {

    return teamsData.sort(function(a,b){return parseInt(a['wins']) - parseInt(b['wins'])});

  }

  /**
   * Adds a `rank` field to be displayed next to the team name. Dependent on sorted teams list
   */
  function addStandingsRankingNumber (teamsList) {

    let teams = []

    for (let i = 0; i < teamsList.length; i++){
      let currentTeam = teamsList[i];
      currentTeam['rank'] = i + 1;

      teams.push(currentTeam);
    }

    return teams
  }

  return (
    
    <div className='bg-white'>

      <div className='grid grid-cols-1'>

        <div>
          <NavBar />
        </div>

        <div className='text-center p-4 pt-12'>

          <div className='md:text-4xl font-bold pb-4 text-orange-500'>YMBL 2022-2023</div>
          <div className='md:text-4xl font-bold text-orange-500'>Regular Season Standings</div>

        </div>

        <div className='flex flex-col flex-wrap justify-self-center md:m-10 md:p-4 rounded-md divide-y-4 divide-orange-500 border-4 border-orange-500'>
          <StandingsTeamList standingTeams={teams} />
        </div>

      </div>

    </div>  
    
  );
}
