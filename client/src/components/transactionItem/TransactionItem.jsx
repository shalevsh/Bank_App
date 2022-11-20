import React from "react";
import "transactionItem.css"
import axios from "axios"
import * as constants from "../../constants/consts.js";


function TransactionItem(props) {
    const deleteTransaction=()=>{
        axios.delete(`${constants.TRANSACTIONS_URL}${props.transaction.id}`)
        .then(()=>props.fetchData())
    }
    return( 
        <div className="transaction-card">
            <div className="text-card">
                <h4 className={`${props.transactionItem.transaction.amount >0 ? "positive-text" : "negative-text"}`}>{props.transaction.amount}$</h4>
                <h4>{props.transactionItem.category.category}</h4>
                <h4>{props.transactionItem.category.vendor}</h4>
                <button className="transaction-delete-button" onClick={deleteTransaction}>{constants.DELETE}</button>
            </div>
        </div>
        );
}

export default TransactionItem;