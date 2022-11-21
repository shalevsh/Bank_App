import React from "react";
import { useState,useEffect } from "react";
import axios from "axios"
import "operations.css"
import * as constants from "../../constants/consts.js";


function Operations(props) {
        const [categories,setCategories] = useState([])
        const [inputValues,setInputValues] = useState({amount:undefined,vendor:undefined,category:undefined})
        const user_id = props.user.user_id;
        const amount = inputValues.amount;
        const category= inputValues.category;
        const vendor = inputValues.vendor;

        useEffect(()=>{
                axios.get(constants.CATEGORIES_URL).then(res=>{setCategories(res.data)})
            },[])

        const inputHandler=(event)=>{
                const newInputValues={...inputValues}
                let newValue=event.target.value
                if(isNaN(event.target.name)){
                        newValue=Math.abs(newValue)
                }
                newInputValues[event.target.name] = newValue
                setInputValues(newInputValues)
        }

        const clickHandler=(event)=>{
                const is_deposite = !(event.target.name===constants.WITHDRAW)
                if(inputValues.amount && inputValues.vendor && inputValues.category){
                        axios.post(constants.TRANSACTIONS_URL,{
                                user_id,amount,category,vendor,is_deposite
                        }).then(()=>
                        {
                        setInputValues({amount : undefined, vendor : undefined, category : undefined})
                        props.fetchUser();
                })       
                }
        }
    return( 
        <div className="Operations">
                <h2 className="opertaions-title">{constants.INSERT_TRANSACTION}</h2>
                <label>{constants.TRANSACTION_AMOUNT}</label>
                <input name="amount" type="number" className="amount-input" min="0" value={inputValues.amount} onChange={inputHandler} />
                <label>{constants.TRANSACTION_VENDOR}</label>
                <input name="vendor" className="vendor-input" placeholder="TRANSACTION VEDOR" value={inputValues.vendor} onChange={inputHandler}/>
                <label>{constants.TRANSACTION_CATRGORY}</label>
                <select name="category" className="category-input" value={inputValues.category} onChange={inputHandler}>
                        <option value="init">{constants.SELECT_CATEGORY}</option>
                        {
                        categories.map(category=><option value={category} selected>{category}</option>)
                        }
                </select>
                <button className="deposit-button" name="deposit" onClick={clickHandler} >{constants.DEPOSIT}</button>
                <button className="withdraw-button" name="withdraw" onClick={clickHandler}>{constants.WITHDRAW}</button>
        </div>
        );
}

export default Operations;