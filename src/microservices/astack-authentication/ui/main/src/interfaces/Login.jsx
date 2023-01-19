import React from 'react'
import { useState } from 'react';
import { useNavigate } from "react-router-dom";
import axios from 'axios'

export default function Login(){
    const [userLoginId, setUserLoginId] = useState("");
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    const [error, setErrors] = useState([]);
    const [isDisabled, setIsDisabled] = useState(false);

    const nav = useNavigate();

    function createLoginKey () {

        if (!parseInt(userLoginId)){
            setErrors("Invalid Login Id!");
        }
        if (userLoginId.length !== parseInt(userLoginId).toString().length){
            setErrors("Invalid Login Id!");
        }

        let creds = {'password': password, 'login_id': userLoginId};
        let encoded = btoa(JSON.stringify(creds));

        return encoded;
    }

    async function handleSubmission(event) {
        event.preventDefault();

        setIsDisabled(true);
        await axios.post('https://astack-authenticator-3jcqeir73q-uc.a.run.app/admin-stack/beta-v1.0/oauth/authenticator/token', JSON.stringify(
            `grant_type=&username=${username}&password=${createLoginKey()}&scope=&client_id=&client_secret=`
          )).then(
              result => {
                  if (result.data['access_token']){
                      localStorage.setItem("token", result.data['access_token']);
                      nav("/home", {replace: true})
                  }

                  setIsDisabled(false);
                  setErrors(result.data['msg']);
                  
              }
          ).catch(
              err => {
                console.log(err);
                setIsDisabled(false);
              });
    }

    return(
        <div className='bg-gray-800 pb-96'>

            <div className='col-span-2 font-bold p-4 space-x-2 justify-items-stretch'>
                <span className='text-xl md:text-3xl text-orange-500 justify-self-center'>ASTACK</span>
                <span className='text-sm md:text-xl text-white text-center'>Beta</span>
            </div>

            <div className='flex flex-col text-center font-bold text-orange-500 text-5xl font-mono p-10 space-y-10 pb-20 md:pb-40 pt-28'>
                <span>ASTACK PORTAL</span>
                <span>LOGIN</span>
            </div>
            <div className='text-center pb-10 font-bold text-red-600 text-xl'>{error}</div>
            <form className='text-center space-y-10' onSubmit={handleSubmission}>
                <div className='xl:space-x-10 flex flex-col'>
                    <label className='font-mono text-lg md:text-xl lg:text-2xl text-orange-500 font-bold' htmlFor="firstName">Login Id</label>
                    <input 
                        type="password" 
                        name="loginId"
                        value={userLoginId}
                        onChange={(event) => setUserLoginId(event.target.value)}
                        className="ml-10 mr-10 appearance-none bg-transparent border-b-2 border-orange-500 leading-tight focus:outline-none text-lg md:text-xl lg:text-2xl text-center text-white font-mono"
                    />
                </div>
                <div className='xl:space-x-10 flex flex-col'>
                    <label className='font-mono text-lg md:text-xl lg:text-2xl text-orange-500 font-bold' htmlFor="firstName">Username</label>
                    <input 
                        type="text" 
                        name="username"
                        value={username}
                        onChange={(event) => setUsername(event.target.value)}
                        className="ml-10 mr-10 appearance-none bg-transparent border-b-2 border-orange-500 leading-tight focus:outline-none text-lg md:text-xl lg:text-2xl text-center text-white font-mono"
                    />
                </div>
                <div className='xl:space-x-10 flex flex-col'>
                    <label className='font-mono text-lg md:text-xl lg:text-2xl text-orange-500 font-bold' htmlFor="firstName">Password</label>
                    <input 
                        type="password" 
                        name="password"
                        value={password}
                        onChange={(event) => setPassword(event.target.value)}
                        className="ml-10 mr-10 appearance-none bg-transparent border-b-2 border-orange-500 leading-tight focus:outline-none text-lg md:text-xl lg:text-2xl text-center text-white font-mono"
                    />
                </div>
                <button className='bg-transparent p-4 rounded-md font-bold text-2xl text-orange-500 border-2 border-transparent hover:border-orange-500' disabled={isDisabled}>
                    Let's Go
                </button>
            </form>

        </div>
    )
}