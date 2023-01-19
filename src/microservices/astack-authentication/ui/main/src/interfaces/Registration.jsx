import axios from 'axios';
import React from 'react';
import { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';

export default function Registration(){
    const [astackUserKey, setAstackUserKey] = useState("");
    const [firstName, setFirstName] = useState("");
    const [lastName, setLastName] = useState("");
    const [username, setUsername] = useState("");
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const [confirmedPassword, setConfirmedPassword] = useState("");
    const [adminLevel, setAdminLevel] = useState("");
    const [adminPosition, setAdminPosition] = useState("");
    const [isDisabled, setIsDisabled] = useState(false);
    const [error, setError] = useState("");

    const {key} = useParams();

    useEffect(
        () => {
            console.log(key)
            axios.get(`https://astack-authenticator-3jcqeir73q-uc.a.run.app/admin-stack/beta-v1.0/new-admin/add/?admin_request=${key}`
            ).then(
                result => {
                    // may want to verify that result.status == 200
                    console.log(result);
                    let decoded = atob(key);

                    let decodedJSON = JSON.parse(decoded);
                    setAstackUserKey(decodedJSON['login_id']);
                    setAdminLevel(decodedJSON['admin_level']);
                    setAdminPosition(decodedJSON['position']);

                }
            ).catch(
                err => {
                    console.log(err);
                }
            )

        }, []
    )

    async function handleSubmission(event){
        event.preventDefault();

        setIsDisabled(true);
        await axios.post('https://astack-authenticator-3jcqeir73q-uc.a.run.app/admin-stack/beta-v1.0/new-admin/add/', {
            'login_id': astackUserKey,
            'first_name': firstName,
            'last_name': lastName,
            'username':username,
            'email': email,
            'password': password,
            'confirm_password': confirmedPassword,
            'position': adminPosition,
            'astack_right_level': adminLevel
        }).then(
            result => {
                console.log(result.data);
                if (result.data['http_code'].toString() == 200){
                    console.log('Successfully Registered');
                }
                setIsDisabled(false);
                setError(result.data['msg']);
            }
        ).catch(
            err => {
                console.log(err);
                setIsDisabled(false);
            }
        )

    }

    return (
        <div className='grid grid-cols-2 bg-gray-800 p-6 pb-96'>

            <div className='col-span-2 font-bold p-4 space-x-2 justify-items-stretch'>
                <span className='text-3xl text-orange-500 justify-self-center'>ASTACK</span>
                <span className='text-xl text-white text-center'>Beta</span>
            </div>

            <div className='flex flex-col font-bold space-x-10 space-y-10 p-4 text-center mt-40 md:mb-40 font-mono col-span-2 md:col-span-1'>
                <div className='text-5xl xl:text-7xl text-orange-500'>Welcome Admin</div>
                <div className='text-2xl xl:text-4xl text-orange-500'>Lets Get You Started</div>
            </div>
            
            <form className='grid mt-40 space-y-4 pl-6 justify-items-stretch col-span-2 md:col-span-1' onSubmit={handleSubmission}>
                <div className='text-center pb-10 font-bold text-red-600 text-xl'>{error}</div>
                <div className='space-x-10'>
                    <label className='text-lg md:text-xl lg:text-2xl font-mono text-orange-500 font-bold' htmlFor="firstName">Login ID:</label>
                    <label className='text-lg md:text-xl lg:text-2xl text-orange-500 font-bold font-mono'>{astackUserKey}</label>
                </div>
                <div className='xl:space-x-10'>
                    <label className='font-mono text-lg md:text-xl lg:text-2xl text-orange-500 font-bold' htmlFor="firstName">Enter Your First Name</label>
                    <input 
                        type="text" 
                        name="firstName"
                        value={firstName}
                        onChange={(event) => setFirstName(event.target.value)}
                        className="appearance-none bg-transparent border-b-2 border-orange-500 leading-tight focus:outline-none text-lg md:text-xl lg:text-2xl text-center text-white font-mono"
                    />
                </div>
                <div className='xl:space-x-10'>
                    <label className='font-mono text-lg md:text-xl lg:text-2xl text-orange-500 font-bold' htmlFor="firstName">Enter Your Last Name</label>
                    <input 
                        type="text" 
                        name="lastName"
                        value={lastName}
                        onChange={(event) => setLastName(event.target.value)}
                        className="bg-transparent border-b-2 border-orange-500 leading-tight focus:outline-none text-lg md:text-xl lg:text-2xl text-center text-white font-mono"
                    />
                </div>
                <div className='xl:space-x-10'>
                    <label className='font-mono text-lg md:text-xl lg:text-2xl text-orange-500 font-bold' htmlFor="firstName">Enter Your Username</label>
                    <input 
                        type="text" 
                        name="username"
                        value={username}
                        onChange={(event) => setUsername(event.target.value)}
                        className="bg-transparent border-b-2 border-orange-500 leading-tight focus:outline-none text-lg md:text-xl lg:text-2xl text-center text-white font-mono"
                    />
                </div>
                <div className='xl:space-x-10'>
                    <label className='font-mono text-lg md:text-xl lg:text-2xl text-orange-500 font-bold' htmlFor="firstName">Enter Your Email</label>
                    <input 
                        type="text" 
                        name="email"
                        value={email}
                        onChange={(event) => setEmail(event.target.value)}
                        className="bg-transparent border-b-2 border-orange-500 leading-tight focus:outline-none text-lg md:text-xl lg:text-2xl text-center text-white font-mono"
                    />
                </div>
                <div className='xl:space-x-10'>
                    <label className='font-mono text-lg md:text-xl lg:text-2xl text-orange-500 font-bold' htmlFor="firstName">Enter Your Password</label>
                    <input 
                        type="text" 
                        name="password"
                        value={password}
                        onChange={(event) => setPassword(event.target.value)}
                        className="bg-transparent border-b-2 border-orange-500 leading-tight focus:outline-none text-lg md:text-xl lg:text-2xl text-center text-white font-mono"
                    />
                </div>
                <div className='xl:space-x-10'>
                    <label className='font-mono text-lg md:text-xl lg:text-2xl text-orange-500 font-bold' htmlFor="firstName">Confirm Your Password</label>
                    <input 
                        type="text" 
                        name="confirmedPassword"
                        value={confirmedPassword}
                        onChange={(event) => setConfirmedPassword(event.target.value)}
                        className="bg-transparent border-b-2 border-orange-500 leading-tight focus:outline-none text-lg md:text-xl lg:text-2xl text-center text-white font-mono"
                    />
                </div>
                <div className='md:space-x-4 xl:space-x-10'>
                    <label className='font-mono text-lg md:text-xl lg:text-2xl text-orange-500 font-bold' htmlFor="firstName">ASTACK Admin Level:</label>
                    <label className='text-lg md:text-xl lg:text-2xl text-orange-500 font-bold font-mono'>{adminLevel}</label>
                </div>
                <button className='justify-self-center bg-transparent p-4 rounded-md font-bold text-2xl text-orange-500 border-2 border-transparent hover:border-orange-500' disabled={isDisabled}>
                    Let's Go
                </button>
            </form>
        </div>
    )
}