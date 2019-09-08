//增加
function add_two_text(tab_t,ind) {

    // var tab = document.getElementById(id);
    //alert(tab.rows.length)
    var rownum = tab_t.rows.length;// 行数
    var newRow=tab_t.insertRow(rownum);

    var cellname_check = newRow.insertCell(0);
    // cellname.innerHTML="<input type='text' value='' />";
    cellname_check.innerHTML="<td size='5'><input type='checkbox' name='checkbox2' value='checkbox' /></td>";

    var cellname_test1 = newRow.insertCell(1);
    cellname_test1.innerHTML="<input type='text' value='' width='20' size='40'/>";

    var cellname_test2 = newRow.insertCell(2);
    cellname_test2.innerHTML="<input type='text' value=''  width='20px' size='40'/>";
    // cellname.innerHTML="<td align='center' bgcolor='#FFFFFF'><input type='checkbox' name='checkbox2' value='checkbox' /></td>";
    var cellname_test3 = newRow.insertCell(3);
    cellname_test3.innerHTML="<input type='button' name='' id='' onclick='save_two_text(this)' value='保存' />";
}
//保存两列文本
function save_two_text(obj) {
//			alert(obj.parentNode.parentNode.innerHTML)
    var tr = obj.parentNode.parentNode; // 获取的本行的tr
//	alert(tr.cells[0].childNodes[0].value)
//     tr.cells[0].innerHTML = tr.cells[0].childNodes[0].value
    tr.cells[1].innerHTML = tr.cells[1].childNodes[0].value;

    tr.cells[2].innerHTML = tr.cells[2].childNodes[0].value;

    tr.cells[3].innerHTML = "<td size='20' bgcolor='#FFFFFF'><input type='button' name='' id='' onclick='update_two_text(this)' value='修改' /></td>";

}

function update_two_text(obj) {
    var tr = obj.parentNode.parentNode;
    tr.cells[1].innerHTML = "<input type='text' value='"+ tr.cells[1].innerHTML +"' width='20' size='40'/>";;
    tr.cells[2].innerHTML = "<input type='text' value='"+ tr.cells[2].innerHTML +"' width='20' size='40'/>";;
    tr.cells[3].innerHTML = "<input type='button' name='' id='' onclick='save_two_text(this)' value='保存' />";
}

//-----------------------
//增加 formdata
function add_tables_formdata(obj,inde) {
    var rownum = obj.rows.length;// 行数
    var newRow=obj.insertRow(rownum);

    var cellname_check1 = newRow.insertCell(0);
    cellname_check1.innerHTML="<td size='5' bgcolor='#FFFFFF'><input type='checkbox' name='checkbox2' value='' /></td>";

    var cellname_check2 = newRow.insertCell(1);
    cellname_check2.innerHTML="<td size='40' bgcolor='#FFFFFF'><input type='text' value='' width='20' size='40'/></td>";

    var cellname_check3 = newRow.insertCell(2);
    cellname_check3.innerHTML="<td size='' bgcolor='#FFFFFF'><select type='' onchange='upd_text_file(this)' width='14px' value='' size='' ><option value='text'>text</option><option value='file'>file</option></select></td>";

    var cellname_check4 = newRow.insertCell(3);
    cellname_check4.innerHTML="<td size='40' bgcolor='#FFFFFF'><input type='text' value=''  width='20px' size='40'/></td>";

    var cellname_check5 = newRow.insertCell(4);
    cellname_check5.innerHTML="<td size='20' bgcolor='#FFFFFF'><input type='button' name='' id='' onclick='save_form_dat(this)' value='保存' /></td>";

}

//保存数据表格数据 form dat
function save_form_dat(obj){
//			alert(obj.parentNode.parentNode.innerHTML)
    var tr = obj.parentNode.parentNode; // 获取的本行的tr
//	alert(tr.cells[0].childNodes[0].value)
//     tr.cells[0].innerHTML = tr.cells[0].childNodes[0].value
    tr.cells[0].innerHTML = "<td size='5' bgcolor='#FFFFFF'><input type='checkbox' name='checkbox2' value='' /></td>";

    tr.cells[1].innerHTML = tr.cells[1].childNodes[0].value;

    tr.cells[2].innerHTML = tr.cells[2].childNodes[0].value;


    if(tr.cells[2].childNodes[0].textContent == 'file'){

    }else {
        tr.cells[3].innerHTML = tr.cells[3].childNodes[0].value;
    }
    tr.cells[4].innerHTML = "<td size='20' bgcolor='#FFFFFF'><input type='button' name='' id='' onclick='update_form_dat(this)' value='修改' /></td>";

    // var cellname_check5 = tr.insertCell(4);
    // cellname_check5.innerHTML="<td size='20' bgcolor='#FFFFFF'><input type='button' name='' id='' onclick='save(this)' value='修改' /></td>";


    // alert(tr.cells[2].childNodes[0].textContent);
    // tr.cells[3].innerHTML = tr.cells[3].childNodes[0].value

}

//修改
function update_form_dat(obj) {
    var tr = obj.parentNode.parentNode; // 获取的本行的tr
	// alert(tr.cells[2].childNodes[0].textContent)
//     tr.cells[0].innerHTML = tr.cells[0].childNodes[0].value
    tr.cells[0].innerHTML = "<td size='5' bgcolor='#FFFFFF'><input type='checkbox' name='checkbox2' value='' /></td>";

    tr.cells[1].innerHTML = "<td size='40' bgcolor='#FFFFFF'><input type='text' value='" + tr.cells[1].innerHTML +"' width='20' size='40'/></td>";

    // alert(tr.cells[2]);
    // tr.cells[2].innerHTML = "<td size='' bgcolor='#FFFFFF'>" +
    //     "<select type='' onchange='upd_text_file(this)' width='14px' value='" + tr.cells[2].innerHTML +"' size='' >" +
    //     "<option value='text'>text</option><option value='file'>file</option></select></td>";

    // tr.cells[2].attr("file",true); selected='selected'
    // console.log(tr.cells[2].childNodes[0].value);
    // console.log(tr.cells[2].childNodes[0].textContent);
    console.log(tr.cells[2].childNodes[0].value);
    if(tr.cells[2].childNodes[0].value == 'file' || tr.cells[2].childNodes[0].textContent == 'file'){
            tr.cells[2].innerHTML = "<td size='' bgcolor='#FFFFFF'>" +
        "<select type='' onchange='upd_text_file(this)' width='14px' value='" + tr.cells[2].innerHTML +"' size='' >" +
        "<option value='text' >text</option><option value='file' selected='selected'>file</option></select></td>";
        // tr.cells[2].childNodes[0].value = 'file'
        // alert("123");
    }else {

    tr.cells[2].innerHTML = "<td size='' bgcolor='#FFFFFF'>" +
        "<select type='' onchange='upd_text_file(this)' width='14px' value='" + tr.cells[2].innerHTML +"' size='' >" +
        "<option value='text' selected='selected'>text</option><option value='file'>file</option></select></td>";
        tr.cells[3].innerHTML = "<td size='40' bgcolor='#FFFFFF'><input type='text' value='" + tr.cells[3].innerHTML +"'  width='20px' size='40'/></td>";
     }
    tr.cells[4].innerHTML = "<td size='20' bgcolor='#FFFFFF'><input type='button' name='' id='' onclick='save_form_dat(this)' value='保存' /></td>";

}

//-----------------------
//增加 断言

var index_ = []
function add_tables_assert(tab_t,index_s) {
    var rownum = tab_t.rows.length;// 行数
    var newRow=tab_t.insertRow(rownum);
    index_ = index_s;

    var cellname_check = newRow.insertCell(0);
    // cellname.innerHTML="<input type='text' value='' />";
    cellname_check.innerHTML="<td bgcolor='#FFFFFF'><input type='checkbox' name='checkbox2' value='checkbox' /></td>";

    var op_text = '';
    for(var i=0; i< index_s.length;i++){
            op_text += "<option value="+ index_s[i]['value'] +">" + index_s[i]['text'] +"</option>";
        }
    console.log(op_text);
    var cellname_value1 = newRow.insertCell(1);
    cellname_value1.innerHTML= "<td  width='10' editstate='true' bgcolor='#FFFFFF'>" +
        "<select type='' onchange='upd_assert(this)' width='12px' value='' size='' >" +
        op_text +
        "</select></td>";
    // cellname_value1.setAttribute('bgcolor','#FFFFFF');
    // cellname_value1.setAttribute('value','');
    // cellname_value1.setAttribute('title','');
    // cellname_value1.setAttribute('editstate','false');

    var cellname_value2 = newRow.insertCell(2);
    // "<td size='40' bgcolor='#FFFFFF'><input type='text' value=''  width='20px' size='40'/></td>";


    cellname_value2.innerHTML="<td bgcolor='#FFFFFF'><input size='40' type='text' value=''/></td>";
        // "<td style='max-width:40px;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;'></td>";

    // {text:'int',value:'int'},{text:'str', value:'str'},{text:'json', value:'json'}
    var cellname_value3 = newRow.insertCell(3);
    cellname_value3.innerHTML="<td  width='10' editstate='true' bgcolor='#FFFFFF'>" +
        "<select type='' onchange='upd_assert(this)' width='12px' value='' size='' >" +
            "<option value='int'>int</option>" +
            "<option value='str'>str</option>" +
            "<option value='json'>json</option>" +
        "</select></td>";

        var cellname_value4 = newRow.insertCell(4);
    cellname_value4.innerHTML="<td bgcolor='#FFFFFF'><input size='40' type='text' value=''/></td>";

        var cellname_value5 = newRow.insertCell(5);
    cellname_value5.innerHTML="<td size='20' bgcolor='#FFFFFF'><input type='button' name='' id='' onclick='save_tables_assert(this)' value='保存' /></td>";

}

//保存数据表格数据 tables_assert
function save_tables_assert(obj){
//			alert(obj.parentNode.parentNode.innerHTML)
    var tr = obj.parentNode.parentNode; // 获取的本行的tr
//	alert(tr.cells[0].childNodes[0].value)
//     tr.cells[0].innerHTML = tr.cells[0].childNodes[0].value
    tr.cells[0].innerHTML = "<td size='5' bgcolor='#FFFFFF'><input type='checkbox' name='checkbox2' value='' /></td>";

    tr.cells[1].innerHTML = tr.cells[1].childNodes[0].value;

    tr.cells[2].innerHTML = tr.cells[2].childNodes[0].value;
    tr.cells[3].innerHTML = tr.cells[3].childNodes[0].value;
    tr.cells[4].innerHTML = tr.cells[4].childNodes[0].value;

    tr.cells[5].innerHTML = "<td size='20' bgcolor='#FFFFFF'><input type='button' name='' id='' onclick='update_tables_assert(this)' value='修改' /></td>";

}

//修改tables_assert
function update_tables_assert(obj) {
    var tr = obj.parentNode.parentNode; // 获取的本行的tr
	// alert(tr.cells[2].childNodes[0].textContent)
//     tr.cells[0].innerHTML = tr.cells[0].childNodes[0].value
    tr.cells[0].innerHTML = "<td size='5' bgcolor='#FFFFFF'><input type='checkbox' name='checkbox2' value='' /></td>";

    // console.log(index_);
    var op_text = '';

    console.log(tr.cells[1].childNodes[0].textContent);
    for(var i=0; i< index_.length;i++){
        if (index_[i]['value'] == tr.cells[1].childNodes[0].textContent){
            op_text += "<option selected='selected' value="+ index_[i]['value'] +">" + index_[i]['text'] +"</option>";
        }else {
            op_text += "<option value="+ index_[i]['value'] +">" + index_[i]['text'] +"</option>";
        }
        }
    // console.log(op_text);
    tr.cells[1].innerHTML= "<td  width='10' editstate='true' bgcolor='#FFFFFF'>" +
        "<select type='' onchange='upd_assert(this)' width='12px' value='' size='' >" +
        op_text +
        "</select></td>";

    tr.cells[2].innerHTML = "<td bgcolor='#FFFFFF'><input size='40' type='text' value='" + tr.cells[2].innerHTML +"'/></td>";

    var cell_option = '';
    cell3_data = [{'text': 'int', 'value': 'int'},
        {'text': 'str', 'value': 'str'},
        {'text': 'json', 'value': 'json'}
    ];
    for(var lis=0;lis <cell3_data.length;lis++){
        if(cell3_data[lis]['value'] == tr.cells[3].childNodes[0].textContent){
            cell_option += "<option selected='selected' value="+ cell3_data[lis]['value'] +">" + cell3_data[lis]['text'] +"</option>";
        }else {
            cell_option += "<option  value="+ cell3_data[lis]['value'] +">" + cell3_data[lis]['text'] +"</option>";
        }
    }


    tr.cells[3].innerHTML = "<td  width='10' editstate='true' bgcolor='#FFFFFF'>" +
        "<select type=''  width='12px' value='' size='' >" +
            cell_option +
        "</select></td>";

    tr.cells[4].innerHTML = "<td bgcolor='#FFFFFF'><input size='40' type='text' value='" + tr.cells[4].innerHTML + "'/></td>";


    // console.log(tr.cells[2].childNodes[0].value);
    // if(tr.cells[2].childNodes[0].value == 'file' || tr.cells[2].childNodes[0].textContent == 'file'){
    //         tr.cells[2].innerHTML = "<td size='' bgcolor='#FFFFFF'>" +
    //     "<select type='' onchange='upd_text_file(this)' width='14px' value='" + tr.cells[2].innerHTML +"' size='' >" +
    //     "<option value='text' >text</option><option value='file' selected='selected'>file</option></select></td>";
    //     // tr.cells[2].childNodes[0].value = 'file'
    //     // alert("123");
    // }else {
    //
    // tr.cells[2].innerHTML = "<td size='' bgcolor='#FFFFFF'>" +
    //     "<select type='' onchange='upd_text_file(this)' width='14px' value='" + tr.cells[2].innerHTML +"' size='' >" +
    //     "<option value='text' selected='selected'>text</option><option value='file'>file</option></select></td>";
    //     tr.cells[3].innerHTML = "<td size='40' bgcolor='#FFFFFF'><input type='text' value='" + tr.cells[3].innerHTML +"'  width='20px' size='40'/></td>";
    //  }
    tr.cells[5].innerHTML = "<td size='20' bgcolor='#FFFFFF'><input type='button' name='' id='' onclick='save_tables_assert(this)' value='保存' /></td>";

}






function save(obj) {
//			alert(obj.parentNode.parentNode.innerHTML)
    var tr = obj.parentNode.parentNode; // 获取的本行的tr
//	alert(tr.cells[0].childNodes[0].value)
//     tr.cells[0].innerHTML = tr.cells[0].childNodes[0].value
    tr.cells[1].innerHTML = tr.cells[1].childNodes[0].value;

    tr.cells[2].innerHTML = tr.cells[2].childNodes[0].value;

    if (tr.cells[2].childNodes[0].textContent == 'file') {

    } else {
        tr.cells[3].innerHTML = tr.cells[3].childNodes[0].value;
    }
    tr.cells[4].innerHTML = "<td size='20' bgcolor='#FFFFFF'><input type='button' name='' id='' onclick='save(this)' value='修改' /></td>";

}

function upd_text_file(obj){
    // alert(obj.value);
    var tr = obj.parentNode.parentNode;
    if (obj.value == 'text'){
        // tr.cells[1].innerHTML = "<input type='text' value=''  width='20px' size='40'/>";
        tr.cells[3].innerHTML = "<input type='text' value=''  width='20px' size='40'/>";

    }else{
        tr.cells[3].innerHTML = "<input type='file' width='14px' value='' size='' />";
        // tr.cells[1].innerHTML = "<input type='text' value=''  width='20px' size='40'/><input type='button' name='' id='' onclick='save(this)' value='保存' />";
    }


}

function update(obj){
//	alert(obj.parentNode.parentNode.innerHTML)
    var tr = obj.parentNode.parentNode; // 获取的本行的tr
//	alert(tr.cells[0].childNodes[0].value)
    tr.cells[0].innerHTML = "<input type='text' bgcolor='#EFEFEF' value='"+tr.cells[0].innerHTML+"' size='10' />";
    tr.cells[1].innerHTML = "<input type='select' value='"+tr.cells[1].innerHTML+"' size='10' />";
    // value='"+tr.cells[2].innerHTML+"'
    tr.cells[2].innerHTML = "<select type='' width='14px' value='value' size='' ><option value='file'>file</option><option value='text'>text</option></select>";
    tr.cells[4].innerHTML = "<input type='button' name='' onclick='dele(this)' id='' value='删除' /><input type='button' name='' onclick='save(this)' id=''  value='保存' />"
}


//增加file table
function add_table_files(tab_t,ind) {

    // var tab_t = document.getElementById(tab_id);
    // alert(ind);
    var rownum = tab_t.rows.length;// 行数
    var newRow=tab_t.insertRow(rownum);

    var cellname_check = newRow.insertCell(0);
    // cellname.innerHTML="<input type='text' value='' />";
    cellname_check.innerHTML="<td size='5'><input type='checkbox' name='checkbox2' value='checkbox' /></td>";

    var cellname_test1 = newRow.insertCell(1);
    cellname_test1.innerHTML="<td size='40' bgcolor='#FFFFFF'> "+ ind[0] + "</td>";

    var cellname_test2 = newRow.insertCell(2);
    cellname_test2.innerHTML="<td size='40' bgcolor='#FFFFFF'>"+ ind[1] + "</td>";
    // cellname.innerHTML="<td align='center' bgcolor='#FFFFFF'><input type='checkbox' name='checkbox2' value='checkbox' /></td>";
    var cellname_test3 = newRow.insertCell(3);
    cellname_test3.innerHTML="<input type='button' name='' id='' onclick='file_Delete(this)' value='删除' />";
}

function file_Delete(obj) {

    var otr = obj.parentNode.parentNode;
//	var tab = document.getElementById("tab");
//	tab.deleteRow(otr.rowIndex)
    var tab =  otr.parentNode; //自己的父节点 就是table
    tab.removeChild(otr);

}