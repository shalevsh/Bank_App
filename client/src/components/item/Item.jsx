import React from "react";
// import "item.css"
import axios from "axios"
import * as constants from "../../constants/consts.js";
import TransactionItem from "./transactionItem/TransactionItem.jsx";
import CategoryItem from "./categoryItem/CategoryItem.jsx";


function Item(props) {
    const deleteTransaction=()=>{
        axios.delete(`${constants.TRANSACTIONS_URL}${props.transaction.id}`)
        .then(()=>props.fetchData())
    }
    return( 
        <div className="transaction-card">
                <TransactionItem transaction = {props.item.transaction}/>
                <CategoryItem category = {props.item.category}/>
                <button className="transaction-delete-button" onClick={deleteTransaction}>{constants.DELETE}</button>
        </div>
        );
}

export default Item;