/** @odoo-module **/


import { registry } from "@web/core/registry";


class LogOutService {
    constructor(orm) {

        this.orm = orm;
        this.time = this.getTime().then((data)=>data);
        debugger;
        console.log('hello',this.time)
    }

        async getTime() {
            const res = await this.orm.call('res.users', 'get_logout_time');
            return res;
        }

}


export const logOutService = {
    dependencies: ["orm"],
    async: [
        "getTime",
    ],
    start(env, { orm}) {
        return new LogOutService(orm);
    }
};

registry.category("services").add("logOutService", logOutService);
//setTimeout(()=>{
//     location.replace("/web/session/logout")
//}, 2000);