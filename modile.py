if (!window["App"]) throw new Error("Critical Error in Application");
(function m(App) {


    //===========================================================================================================


    function lib() {
        var _windowContainer = null,
        _guid = null,
        _poll = this,
        _name = '',
        _store = null;

        var header, panel;

        var save = function(){ //Функция сохранения изменений в анкете
            if (!panel.container['form'].pharmId) return false;

            var modifyData = '';

            $.each(_store.getModifiedRecords(), function(index, rec){
                $.each(rec.modified, function(name){
                    modifyData += '&values['+index+']['+name+']=' + rec.data[name];
                });
                modifyData += '&id['+index+']=' + rec.id;
            });
