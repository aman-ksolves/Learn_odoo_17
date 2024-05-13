/* @odoo-module */
import { useState } from "@odoo/owl";
import { patch } from "@web/core/utils/patch";
import { SwitchCompanyMenu} from "@web/webclient/switch_company_menu/switch_company_menu";

patch(SwitchCompanyMenu.prototype, {
    setup() {
        super.setup(...arguments);
        this.inputValue = useState({ name : ""});
      },
    selectAll(){
        for (let companyId in this.companyService.allowedCompanies){
            let comp = this.companyService.allowedCompanies[companyId];
            this.companySelector._selectCompany(comp.id)
        }
        this.companySelector._apply()
    },
    deselectAll(){
        this.companySelector.switchCompany("loginto",this.companyService.currentCompany.id)
    },
    onKeyUpFunction(e){
        this.inputValue.name = e.target.value;
    }
});