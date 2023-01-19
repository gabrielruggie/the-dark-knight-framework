import axios from 'axios';
import React from 'react';
import { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import TeamList from './components/TeamList';

/**
 * 
 */
export default function StatPadder () {
    const [showForm, setShowForm] = useState(false);
    const [showInstr, setShowInstr] = useState(false);
    const [updateStats, setUpdateStats] = useState("");
    const [Error, setError] = useState("")

    const nav = useNavigate();

    // Players
    const [player1, setPlayer1] = useState("")
    const[player2, setPlayer2] = useState("")
    const [player3, setPlayer3] = useState("")
    const [player4, setPlayer4] = useState("")
    const [player5, setPlayer5] = useState("")
    const [player6, setPlayer6] = useState("")
    const [player7, setPlayer7] = useState("")
    const [player8, setPlayer8] = useState("")
    const [player9, setPlayer9] = useState("")
    const [player10, setPlayer10] = useState("")
    const [player11, setPlayer11] = useState("")
    const [player12, setPlayer12] = useState("")
    const [player13, setPlayer13] = useState("")
    const [player14, setPlayer14] = useState("")
    const [player15, setPlayer15] = useState("")
    const [player16, setPlayer16] = useState("")
    const [player17, setPlayer17] = useState("")
    const [player18, setPlayer18] = useState("")
    const [player19, setPlayer19] = useState("")
    const [player20, setPlayer20] = useState("")

    //const [roster, setRoster] = useState([])

    // Team Form Info
    const [teamName, setTeamName] = useState("");
    const [teamMap, setTeamMap] = useState([]);

    useEffect(()=>{
        const onLoad = async() => {
            axios({
                method: "GET",
                url: "https://astack-authenticator-3jcqeir73q-uc.a.run.app/admin-stack/beta-v1.0/oauth/authenticator/verify-astack-admin-token",
                headers: {
                    Authorization: "bearer "+localStorage.getItem("token")
                }
            }).then(
                result => {
                    //setFirstname(result.data['username']);
                    // Don't do anything on success yet...
                    
                }).catch(
                    () => {
                        localStorage.removeItem("token");
                        nav("/login", {replace: true});
                }
                )
            }
            onLoad()
        },[]
    )

    useEffect(

        () => {
        const onLoad = async () => {
            axios({
            method: "GET",
            url: "https://ymbl-query-backend-3jcqeir73q-uc.a.run.app/ymbl/stats"
            }).then(
            result => 
            {
                let data = sortPlayerData(result.data);
                setTeamMap(Object.values(data));

            }).catch();
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
    /** 
     * 
     */
    async function uploadAndDisableEditing (event) {
        event.preventDefault();
        
        var rroster = [player1, player2, player3, player4, player5, player6, player7, player8, player9, player10, player11, player12, player13, player14, player15, player16, player17, player18, player19, player20]
        // var rosterTrimmed = []
        // for (var i = 0; i < roster.length-1; i++){
        //     if ( !roster[i+1].includes(roster[i]) ){
        //         rosterTrimmed.push(roster[i]);
        //     }
        // }
        // // Always push last name on roster
        // rosterTrimmed.push(roster[roster.length-1])

        var rosterTrimmed = []
        for (var i = 0; i < rroster.length; i++){
            if (rroster[i].length > 0) {
                rosterTrimmed.push(rroster[i])
            }
        }
        setUpdateStats("disabled");
        await axios.post('https://ymbl-query-backend-3jcqeir73q-uc.a.run.app/ymbl/sendstats-new-team', {
            // Send team name to backend and have them deal with it
            // Don't query database if something is wrong with team name -> instead send failed response back with msg
            'team_name': teamName,
            'roster': rosterTrimmed
        }).then(
          result => {               
            // Refresh page on successful creation
            window.location.reload();
        }
        )
        .catch(
            err => {
                setUpdateStats("");
                setError(err.response.data)
            }
            );
    }

    const redirectHome = () => {
        nav("/home", {replace: true})
    }

    const displayForm = () => {
        setShowForm(!showForm);
    }

    const displayInstructions = () => {
        setShowInstr(!showInstr);
    }

    return(
        <div className=''>

            <div className='bg-gray-800 grid grid-cols-2 font-bold p-4 justify-items-stretch'>
                <div className='text-left'>
                    <span className='text-xl md:text-3xl text-orange-500 justify-self-center'>ASTACK</span>
                    <span className='text-sm md:text-xl text-white text-center pl-2'>Beta</span>
                </div>
                <div className='text-right text-white text-3xl pr-4'>
                    <a className='hover:text-gray-300 cursor-pointer' onClick={redirectHome}>
                        Home
                    </a>
                </div>
            </div>

            <div className='p-8 space-x-4'>
                <button className='border-orange-500 border-2 p-4 bg-transparent hover:bg-orange-500 hover:text-white rounded-md text-orange-500 text-3xl font-bold' onClick={displayForm}>
                    + TEAM
                </button>
                <button className='border-orange-500 border-2 p-4 bg-transparent hover:bg-orange-500 hover:text-white rounded-md text-orange-500 text-3xl font-bold' onClick={displayInstructions}>
                    READ ME
                </button>
            </div>
            {showInstr && (
                <div className='m-10 font-bold border-2 p-8 border-orange-400 rounded-md'>
                    <div className='text-4xl text-gray-800 pb-2 underline'>ADDING A TEAM</div>
                    <div className='pl-4 pt-2 pb-10'>
                        <div className='text-xl pb-2'>To add a team, click on the +Team button above.</div>
                        <div className='text-xl pb-2'>Enter the Team Name in the first input following the formula: </div>
                        <div className='text-xl text-orange-500 pb-2'>(Church Name) (Grade Abreviation) (Team Captain Last Name)</div>
                        <div className='text-xl pb-2'>Examples: St. Luke Sr Ruggie, Ascension Jr Smith, St.Giles Soph James, St. Leonard Frosh Davis</div>
                        <div className='text-xl '>Remember to include both the first and last names of each player!</div>
                    </div>
                    <div className='text-4xl text-gray-800 pb-2 underline'>UPDATING PLAYER STATS</div>
                    <div className='pl-4 pt-2'>
                        <div className='text-xl pb-2'>The stats displayed in Stat Padder will always be TOTALs not averages</div>
                        <div className='text-xl pb-2'>Thus, in order for averages to appear accurately on the YMBL website, the games played column must be accurate</div>
                        <div className='text-xl pb-2'>To increase a player's total stat column, simply enter a positive number. Said number will be added automatcially by Stat Padder</div>
                        <div className='text-xl '>To decrease a player's total stat column, enter a negative number to be added by Stat Padder!</div>
                    </div>
                </div>
                
            )}
            {showForm && (
                <div className='grid grid-cols-3 m-4'>
                    <form className='col-start-2 col-span-1 space-x-4 space-y-4 p-10 border-orange-500 flex flex-col text-center font-bold text-xl border-2'>
                        <label htmlFor="">Team Name</label>
                        <input type="text"
                        disabled={updateStats}
                        onChange={(event) => setTeamName(event.target.value)}
                        className='m-auto bg-blue-100 rounded-md'/>
                        <label htmlFor="">Player 1 Name</label>
                        <input type="text"
                        disabled={updateStats}
                        onChange={(event) => setPlayer1(event.target.value)}
                        className='m-auto bg-blue-100 rounded-md'/>
                        <label htmlFor="">Player 2 Name</label>
                        <input type="text"
                        disabled={updateStats}
                        onChange={(event) => setPlayer2(event.target.value)}
                        className='m-auto bg-blue-100 rounded-md'/>
                        <label htmlFor="">Player 3 Name</label>
                        <input type="text"
                        disabled={updateStats}
                        onChange={(event) => setPlayer3(event.target.value)}
                        className='m-auto bg-blue-100 rounded-md'/>
                        <label htmlFor="">Player 4 Name</label>
                        <input type="text"
                        disabled={updateStats}
                        onChange={(event) => setPlayer4(event.target.value)}
                        className='m-auto bg-blue-100 rounded-md'/>
                        <label htmlFor="">Player 5 Name</label>
                        <input type="text"
                        disabled={updateStats}
                        onChange={(event) => setPlayer5(event.target.value)}
                        className='m-auto bg-blue-100 rounded-md'/>
                        <label htmlFor="">Player 6 Name</label>
                        <input type="text"
                        disabled={updateStats}
                        onChange={(event) => setPlayer6(event.target.value)}
                        className='m-auto bg-blue-100 rounded-md'/>
                        <label htmlFor="">Player 7 Name</label>
                        <input type="text"
                        disabled={updateStats}
                        onChange={(event) => setPlayer7(event.target.value)}
                        className='m-auto bg-blue-100 rounded-md'/>
                        <label htmlFor="">Player 8 Name</label>
                        <input type="text"
                        disabled={updateStats}
                        onChange={(event) => setPlayer8(event.target.value)}
                        className='m-auto bg-blue-100 rounded-md'/>
                        <label htmlFor="">Player 9 Name</label>
                        <input type="text"
                        disabled={updateStats}
                        onChange={(event) => setPlayer9(event.target.value)}
                        className='m-auto bg-blue-100 rounded-md'/>
                        <label htmlFor="">Player 10 Name</label>
                        <input type="text"
                        disabled={updateStats}
                        onChange={(event) => setPlayer10(event.target.value)}
                        className='m-auto bg-blue-100 rounded-md'/>
                        <label htmlFor="">Player 11 Name</label>
                        <input type="text"
                        disabled={updateStats}
                        onChange={(event) => setPlayer11(event.target.value)}
                        className='m-auto bg-blue-100 rounded-md'/>
                        <label htmlFor="">Player 12 Name</label>
                        <input type="text"
                        disabled={updateStats}
                        onChange={(event) => setPlayer12(event.target.value)}
                        className='m-auto bg-blue-100 rounded-md'/>
                        <label htmlFor="">Player 13 Name</label>
                        <input type="text"
                        disabled={updateStats}
                        onChange={(event) => setPlayer13(event.target.value)}
                        className='m-auto bg-blue-100 rounded-md'/>
                        <label htmlFor="">Player 14 Name</label>
                        <input type="text"
                        disabled={updateStats}
                        onChange={(event) => setPlayer14(event.target.value)}
                        className='m-auto bg-blue-100 rounded-md'/>
                        <label htmlFor="">Player 15 Name</label>
                        <input type="text"
                        disabled={updateStats}
                        onChange={(event) => setPlayer15(event.target.value)}
                        className='m-auto bg-blue-100 rounded-md'/>
                        <label htmlFor="">Player 16 Name</label>
                        <input type="text"
                        disabled={updateStats}
                        onChange={(event) => setPlayer16(event.target.value)}
                        className='m-auto bg-blue-100 rounded-md'/>
                        <label htmlFor="">Player 17 Name</label>
                        <input type="text"
                        disabled={updateStats}
                        onChange={(event) => setPlayer17(event.target.value)}
                        className='m-auto bg-blue-100 rounded-md'/>
                        <label htmlFor="">Player 18 Name</label>
                        <input type="text"
                        disabled={updateStats}
                        onChange={(event) => setPlayer18(event.target.value)}
                        className='m-auto bg-blue-100 rounded-md'/>
                        <label htmlFor="">Player 19 Name</label>
                        <input type="text"
                        disabled={updateStats}
                        onChange={(event) => setPlayer19(event.target.value)}
                        className='m-auto bg-blue-100 rounded-md'/>
                        <label htmlFor="">Player 20 Name</label>
                        <input type="text"
                        disabled={updateStats}
                        onChange={(event) => setPlayer20(event.target.value)}
                        className='m-auto bg-blue-100 rounded-md'/>
                        <button 
                        disabled={updateStats}
                        className='text-4xl text-orange-500 font-bold border-2 border-orange-500 rounded-md hover:bg-orange-500 hover:text-white'
                        onClick={(event) => uploadAndDisableEditing(event)}
                        >
                            Submit
                        </button>
                    </form>
                </div>
                
            )}
            <div className='text-red-600 font-bold font-mono text-xl p-1'>{Error}</div>

            <div className='bg-white'>

                <div className='grid grid-cols-1'>

                    <div className='md:m-10 space-y-4'>
                        <TeamList teamMap={teamMap}/>
                    </div>

                </div>

            </div>  

        </div>
    )
}