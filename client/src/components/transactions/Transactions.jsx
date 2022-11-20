import React,{ useState,useEffect } from "react";
import axios from "axios"
import Item from "../item/Item";
import "transactions.css"
import Transaction from "../../models/Transaction";
import Category from "../../models/Category";
import * as constants from "../../constants/consts.js";


function Transactions() {
    const [data, setData] = useState([]);

    const fetchData=async()=>{
        const res = await axios.get(constants.TRANSACTIONS_URL)

        setData(res.data.map( 
            (obj)=>{ 
                return(
                    {
                     transaction : new Transaction(obj.transaction_id,obj.amount,obj.is_deposite),
                     category : new Category(obj.category_id,obj.category,obj.vendor)
                    }
                )    
                }
                    ));
}

    useEffect(()=>{
        fetchData()
    },[])

    return <div className="transactions">{data.map(obj=><Item
     key={obj.transaction.id} item={obj} fetchData={fetchData} />)}</div>;


}
export default Transactions;