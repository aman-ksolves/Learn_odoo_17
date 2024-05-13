/** @odoo-module **/

import { Component,useState,onWillStart } from "@odoo/owl";
import { registry } from "@web/core/registry";
import { useService } from "@web/core/utils/hooks";

class LogOutTimeComp extends Component{
    static template = 'custom_user.LogOutTimeComp';
    setup(){
        console.log('hello doc',document);
        this.state = useState({count:0});
        this.orm = useService("orm");
        this.rpc = useService("rpc");
        this.effect = useService("effect");
        onWillStart(async () => {
             const result = await this.rpc("/get_user_time/timer");
             this.state.countUpTo = result;
        });


        console.log('hello doc END',document);
        setInterval(()=>{
            this.state.count ++;
            this.checkCount();
//            if(this.state.count === 5){
//                this.effect.add({
//                    type:"rainbow_man",
//                    message:"Count is 5",
//
//                })
//            }
        },1000);

        document.onmousemove = ()=>{
            console.log('mouse move')
            this.state.count = 0;
        }
    }
    checkCount(){
        if(this.state.count == this.state.countUpTo){
             location.replace("/web/session/logout")
        }
    }

}

registry.category('systray')
        .add('custom_user.LogOutTimeComp', {Component:LogOutTimeComp},{sequence:25})
