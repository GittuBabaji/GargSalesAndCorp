document.addEventListener('DOMContentLoaded', () => {
    const tables = document.querySelectorAll('.content table');
    
    tables.forEach(table => {
        // 1. Add Filter Input
        const filterWrapper = document.createElement('div');
        filterWrapper.style.marginBottom = '15px';
        filterWrapper.style.display = 'flex';
        filterWrapper.style.justifyContent = 'flex-end';
        
        const filterInput = document.createElement('input');
        filterInput.type = 'text';
        filterInput.placeholder = 'Search / Filter records...';
        filterInput.style.padding = '8px 12px';
        filterInput.style.border = '1px solid #cbd5e1';
        filterInput.style.borderRadius = '6px';
        filterInput.style.minWidth = '250px';
        filterInput.style.outline = 'none';
        
        filterInput.addEventListener('focus', () => filterInput.style.borderColor = '#3b82f6');
        filterInput.addEventListener('blur', () => filterInput.style.borderColor = '#cbd5e1');

        filterWrapper.appendChild(filterInput);
        table.parentNode.insertBefore(filterWrapper, table);

        const tbody = table.querySelector('tbody') || table;
        const rows = Array.from(tbody.querySelectorAll('tr')).filter(row => !row.querySelector('th'));

        // Filter Logic
        filterInput.addEventListener('input', (e) => {
            const term = e.target.value.toLowerCase();
            rows.forEach(row => {
                const text = row.textContent.toLowerCase();
                row.style.display = text.includes(term) ? '' : 'none';
            });
        });

        // 2. Add Sorting Logic
        const headers = table.querySelectorAll('th');
        headers.forEach((header, index) => {
            header.style.cursor = 'pointer';
            header.title = 'Click to sort';
            
            // Add a sort icon placeholder
            const icon = document.createElement('span');
            icon.innerHTML = ' &#8597;'; // Up/down arrow
            icon.style.opacity = '0.3';
            icon.style.fontSize = '0.8em';
            icon.style.marginLeft = '5px';
            header.appendChild(icon);

            let asc = true;
            header.addEventListener('click', () => {
                // Reset icons
                headers.forEach(h => {
                    const span = h.querySelector('span');
                    if (span) {
                        span.innerHTML = ' &#8597;';
                        span.style.opacity = '0.3';
                    }
                });

                // Set active icon
                icon.innerHTML = asc ? ' &#8593;' : ' &#8595;';
                icon.style.opacity = '1';

                const sortedRows = rows.sort((a, b) => {
                    const aCol = a.querySelectorAll('td')[index];
                    const bCol = b.querySelectorAll('td')[index];
                    
                    if (!aCol || !bCol) return 0;
                    
                    const aText = aCol.textContent.trim();
                    const bText = bCol.textContent.trim();
                    
                    // Try numeric sort first
                    const aNum = parseFloat(aText.replace(/[^0-9.-]+/g,""));
                    const bNum = parseFloat(bText.replace(/[^0-9.-]+/g,""));
                    
                    if (!isNaN(aNum) && !isNaN(bNum) && aText.match(/^[0-9.,$-]+$/)) {
                        return asc ? aNum - bNum : bNum - aNum;
                    }
                    
                    // Fallback to string sort
                    return asc ? aText.localeCompare(bText) : bText.localeCompare(aText);
                });

                // Append sorted rows to tbody
                sortedRows.forEach(row => tbody.appendChild(row));
                asc = !asc;
            });
        });
    });
});
