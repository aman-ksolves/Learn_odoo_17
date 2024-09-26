/** @odoo-module **/
import { FormController } from "@web/views/form/form_controller";
import { formView } from '@web/views/form/form_view';
import { registry } from "@web/core/registry";

import { Component } from "@odoo/owl";
import { Dialog } from "@web/core/dialog/dialog";
import { _t } from "@web/core/l10n/translation";
//import { jsClassDialog } from "@blog_js_class/js/js_blog_dialog";

export class jsClassDialog extends Component{
    clickClose() {
        this.props.close()
    }
}
jsClassDialog.template = "blog_js_class.infoDialog";
jsClassDialog.components = { Dialog };
jsClassDialog.title = _t("Model Info"),
jsClassDialog.props = {
    confirmLabel: { type: String, optional: true },
    confirmClass: { type: String, optional: true },
    resModel: { type: String, optional: true },
    tools: Object,
    close: { type: Function, optional: true },
    };
jsClassDialog.defaultProps = {
    confirmLabel: _t("Close"),
    confirmClass: "btn-primary",
};

class jsClassModelInfo extends FormController {
   actionInfoForm(){
       this.env.services.dialog.add(jsClassDialog, {
           resModel: this.props.resModel,
           resDesc: "This is a demo pop-up; feel free to customize the functionality to meet your requirements."
       });
   }
}
jsClassModelInfo.template = "blog_js_class.modelInfoBtn";
export const modelInfoView = {
   ...formView,
   Controller: jsClassModelInfo,
};
registry.category("views").add("model_info", modelInfoView);