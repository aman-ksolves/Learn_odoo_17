/* @odoo-module */

import { patch } from "@web/core/utils/patch";
import { SwitchCompanyMenu} from "@web/webclient/switch_company_menu/switch_company_menu";

patch(SwitchCompanyMenu.prototype, {
    selectAll(){
        for (let companyId in this.companyService.allowedCompanies){
            let comp = this.companyService.allowedCompanies[companyId];
            this.companySelector._selectCompany(comp.id)
        }
        this.companySelector._apply()
    },
    deselectAll(){
        this.companySelector.switchCompany("loginto",this.companyService.currentCompany.id)
    }
});